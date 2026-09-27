from services.ai_service import ai_service, RuleBasedAIProvider

def test_rule_based_ai_summarizer():
    text = "ToolHub is a free online tools website. It is privacy-friendly. Data is processed locally inside the browser. Users love fast tools."
    summary = ai_service.summarize(text)
    assert summary is not None
    assert len(summary) > 0

def test_rule_based_ai_rewriter():
    text = "Basically, we need to convert this text in order to make it concise."
    rewritten = ai_service.rewrite(text, style="concise")
    assert rewritten is not None

def test_rule_based_ai_questions():
    text = "Photosynthesis is the process by which green plants convert light energy into chemical energy."
    questions = ai_service.generate_questions(text, count=2)
    assert isinstance(questions, list)
    assert len(questions) > 0
    assert "question" in questions[0]
