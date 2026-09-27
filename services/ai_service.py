"""
Extensible AI Service Interface for ToolHub.
Supports pluggable providers (Default/Local Rule Engine, OpenAI, Open-source API).
Falls back gracefully if external API keys are not configured.
"""
import os
import re
import requests

class BaseAIProvider:
    """Base interface for all AI Providers."""
    def summarize(self, text, max_length=150):
        raise NotImplementedError
    def rewrite(self, text, style="clear"):
        raise NotImplementedError
    def explain(self, text, level="simple"):
        raise NotImplementedError
    def generate_questions(self, text, count=5):
        raise NotImplementedError

class RuleBasedAIProvider(BaseAIProvider):
    """
    Local privacy-first rule engine fallback.
    Performs NLP text analysis without external API dependencies.
    """
    def summarize(self, text, max_length=150):
        sentences = [s.strip() for s in re.split(r'(?<=[.!?]) +', text) if len(s.strip()) > 10]
        if not sentences:
            return "Text is too short to summarize."
        # Pick top sentences based on key term frequency
        words = re.findall(r'\w+', text.lower())
        stopwords = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'is', 'was', 'are', 'were', 'it', 'this', 'that'}
        freq = {}
        for w in words:
            if w not in stopwords:
                freq[w] = freq.get(w, 0) + 1
        
        scored_sentences = []
        for s in sentences:
            score = sum(freq.get(w, 0) for w in re.findall(r'\w+', s.lower()))
            scored_sentences.append((score, s))
        
        scored_sentences.sort(key=lambda x: x[0], reverse=True)
        summary_sentences = [s[1] for s in scored_sentences[:min(3, len(sentences))]]
        
        # Maintain logical order
        summary = " ".join([s for s in sentences if s in summary_sentences])
        return summary if summary else text[:max_length]

    def rewrite(self, text, style="clear"):
        sentences = re.split(r'(?<=[.!?]) +', text)
        rewritten = []
        for s in sentences:
            s_clean = s.strip()
            if not s_clean:
                continue
            if style == "concise":
                # Remove filler words
                s_clean = re.sub(r'\b(basically|actually|literally|in order to|due to the fact that)\b', '', s_clean, flags=re.IGNORECASE)
                s_clean = re.sub(r'\s+', ' ', s_clean)
            elif style == "formal":
                s_clean = s_clean.replace("don't", "do not").replace("can't", "cannot").replace("won't", "will not")
            elif style == "creative":
                s_clean = f"✨ {s_clean}"
            rewritten.append(s_clean)
        return " ".join(rewritten)

    def explain(self, text, level="simple"):
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        explanation = [
            "### 💡 Key Concept Breakdown",
            f"**Core Topic Summary:** {self.summarize(text, max_length=100)}",
            "",
            "**Key Elements Explained:**"
        ]
        for idx, line in enumerate(lines[:4], 1):
            explanation.append(f"{idx}. **Point {idx}:** {line[:120]}...")
        explanation.append("\n*Note: Processed with local heuristic analysis. Connect OpenAI API key in .env for deep generative explanations.*")
        return "\n".join(explanation)

    def generate_questions(self, text, count=5):
        sentences = [s.strip() for s in re.split(r'(?<=[.!?]) +', text) if len(s.strip()) > 20]
        questions = []
        for idx, sentence in enumerate(sentences[:count], 1):
            words = sentence.split()
            if len(words) > 5:
                keywords = [w for w in words if len(w) > 4 and w.lower() not in {'their', 'there', 'which', 'about', 'would', 'could'}]
                target_word = keywords[0] if keywords else words[0]
                q_text = sentence.replace(target_word, "_______")
                questions.append({
                    "number": idx,
                    "question": f"Fill in the blank: \"{q_text}\"",
                    "answer": target_word.strip(".,!?")
                })
            else:
                questions.append({
                    "number": idx,
                    "question": f"What is the main significance of: \"{sentence}\"?",
                    "answer": sentence
                })
        return questions

class OpenAIProvider(BaseAIProvider):
    """OpenAI API Integration Provider."""
    def __init__(self, api_key):
        self.api_key = api_key

    def _call_gpt(self, system_prompt, user_text):
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_text}
            ],
            "temperature": 0.7
        }
        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=10)
            if resp.status_code == 200:
                return resp.json()['choices'][0]['message']['content'].strip()
            else:
                # Fallback on API error
                return None
        except Exception:
            return None

    def summarize(self, text, max_length=150):
        result = self._call_gpt("You are a helpful AI summarizer. Summarize the text concisely in bullet points.", text)
        if result:
            return result
        return RuleBasedAIProvider().summarize(text, max_length)

    def rewrite(self, text, style="clear"):
        result = self._call_gpt(f"You are a professional text editor. Rewrite the following text in a {style} style.", text)
        if result:
            return result
        return RuleBasedAIProvider().rewrite(text, style)

    def explain(self, text, level="simple"):
        result = self._call_gpt(f"Explain the following concept or code in {level} terms for a student.", text)
        if result:
            return result
        return RuleBasedAIProvider().explain(text, level)

    def generate_questions(self, text, count=5):
        result = self._call_gpt(f"Generate {count} quiz questions and answers based on this text. Format as JSON list of objects with fields question and answer.", text)
        if result:
            import json
            try:
                data = json.loads(result)
                return [{"number": i+1, "question": item["question"], "answer": item["answer"]} for i, item in enumerate(data)]
            except Exception:
                pass
        return RuleBasedAIProvider().generate_questions(text, count)


class AIService:
    """Service Gateway that routes requests to the configured provider."""
    def __init__(self, provider_type=None, api_key=None):
        api_key = api_key or os.getenv('OPENAI_API_KEY', '')
        provider_type = provider_type or os.getenv('AI_PROVIDER', 'default')

        if provider_type == 'openai' and api_key:
            self.provider = OpenAIProvider(api_key)
        else:
            self.provider = RuleBasedAIProvider()

    def summarize(self, text):
        return self.provider.summarize(text)

    def rewrite(self, text, style="clear"):
        return self.provider.rewrite(text, style)

    def explain(self, text, level="simple"):
        return self.provider.explain(text, level)

    def generate_questions(self, text, count=5):
        return self.provider.generate_questions(text, count)

ai_service = AIService()
