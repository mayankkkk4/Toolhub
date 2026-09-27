/**
 * Text Tools Implementation Module
 */

window.TextTools = {
  // 1. Word Counter
  analyzeText: function(text) {
    if (!text) {
      return { words: 0, chars: 0, charsNoSpaces: 0, sentences: 0, paragraphs: 0, readingTime: '0 min' };
    }

    const trimmed = text.trim();
    const words = trimmed ? trimmed.split(/\s+/).filter(Boolean).length : 0;
    const chars = text.length;
    const charsNoSpaces = text.replace(/\s+/g, '').length;
    const sentences = trimmed ? (text.match(/[.!?]+(\s|$)/g) || []).length || 1 : 0;
    const paragraphs = trimmed ? text.split(/\n+/).filter(p => p.trim().length > 0).length : 0;
    
    // Average reading speed: 200 words per minute
    const minutes = Math.ceil(words / 200);
    const readingTime = words === 0 ? '0 min' : `${minutes} min read`;

    return {
      words,
      chars,
      charsNoSpaces,
      sentences,
      paragraphs,
      readingTime
    };
  },

  // 2. Text Case Converter
  convertCase: function(text, targetCase) {
    if (!text) return '';
    switch (targetCase) {
      case 'uppercase':
        return text.toUpperCase();
      case 'lowercase':
        return text.toLowerCase();
      case 'titlecase':
        return text.toLowerCase().split(' ').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
      case 'sentencecase':
        return text.toLowerCase().replace(/(^\s*|[.!?]\s+)([a-z])/g, (m, p1, p2) => p1 + p2.toUpperCase());
      case 'camelcase':
        return text.toLowerCase().replace(/[^a-zA-Z0-9]+(.)/g, (m, chr) => chr.toUpperCase()).replace(/^[A-Z]/, c => c.toLowerCase());
      case 'pascalcase':
        return text.toLowerCase().replace(/(?:^|[^a-zA-Z0-9]+)(.)/g, (m, chr) => chr.toUpperCase());
      case 'snake_case':
        return text.match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g).map(x => x.toLowerCase()).join('_');
      case 'kebab-case':
        return text.match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g).map(x => x.toLowerCase()).join('-');
      default:
        return text;
    }
  },

  // 3. Remove Duplicate Lines
  removeDuplicateLines: function(text, caseSensitive = true, trimLines = true) {
    let lines = text.split('\n');
    if (trimLines) lines = lines.map(l => l.trim());
    
    const seen = new Set();
    const result = [];
    for (const line of lines) {
      const key = caseSensitive ? line : line.toLowerCase();
      if (!seen.has(key)) {
        seen.add(key);
        result.push(line);
      }
    }
    return result.join('\n');
  },

  // 4. Sort Lines
  sortLines: function(text, order = 'a-z', numeric = false) {
    let lines = text.split('\n');
    lines.sort((a, b) => {
      if (numeric) {
        const numA = parseFloat(a) || 0;
        const numB = parseFloat(b) || 0;
        return order === 'a-z' ? numA - numB : numB - numA;
      }
      return order === 'a-z' ? a.localeCompare(b) : b.localeCompare(a);
    });
    return lines.join('\n');
  },

  // 5. Find & Replace
  findAndReplace: function(text, findStr, replaceStr, isRegex = false, matchCase = true) {
    if (!findStr) return text;
    try {
      if (isRegex) {
        const flags = matchCase ? 'g' : 'gi';
        const regex = new RegExp(findStr, flags);
        return text.replace(regex, replaceStr);
      } else {
        const flags = matchCase ? 'g' : 'gi';
        const regex = new RegExp(findStr.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), flags);
        return text.replace(regex, replaceStr);
      }
    } catch (err) {
      return text;
    }
  },

  // 6. Text Diff Computation
  computeDiff: function(text1, text2) {
    const lines1 = text1.split('\n');
    const lines2 = text2.split('\n');

    let html1 = '', html2 = '';
    const maxLen = Math.max(lines1.length, lines2.length);

    for (let i = 0; i < maxLen; i++) {
      const l1 = lines1[i] !== undefined ? lines1[i] : '';
      const l2 = lines2[i] !== undefined ? lines2[i] : '';

      if (l1 === l2) {
        html1 += `<div>${escapeHtml(l1) || '&nbsp;'}</div>`;
        html2 += `<div>${escapeHtml(l2) || '&nbsp;'}</div>`;
      } else {
        if (l1) html1 += `<div class="diff-del">- ${escapeHtml(l1)}</div>`;
        if (l2) html2 += `<div class="diff-add">+ ${escapeHtml(l2)}</div>`;
      }
    }

    return { leftHtml: html1, rightHtml: html2 };
  },

  // 7. Lorem Ipsum Generator
  generateLorem: function(type = 'paragraphs', count = 3) {
    const words = ["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit", "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua", "enim", "ad", "minim", "veniam", "quis", "nostrud", "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "ea", "commodo", "consequat"];
    
    if (type === 'words') {
      const res = [];
      for (let i = 0; i < count; i++) res.push(words[i % words.length]);
      return res.join(' ');
    } else if (type === 'sentences') {
      const res = [];
      for (let i = 0; i < count; i++) {
        let s = [];
        for (let j = 0; j < 10; j++) s.push(words[(i*10 + j) % words.length]);
        res.push(s.join(' ') + '.');
      }
      return res.join(' ');
    } else {
      const paragraphs = [];
      for (let p = 0; p < count; p++) {
        let pSentences = [];
        for (let s = 0; s < 4; s++) {
          let sentenceWords = [];
          for (let w = 0; w < 10; w++) sentenceWords.push(words[(p*40 + s*10 + w) % words.length]);
          let sentence = sentenceWords.join(' ');
          pSentences.push(sentence.charAt(0).toUpperCase() + sentence.slice(1) + '.');
        }
        paragraphs.push(pSentences.join(' '));
      }
      return paragraphs.join('\n\n');
    }
  }
};
