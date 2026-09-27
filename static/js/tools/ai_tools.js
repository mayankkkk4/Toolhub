/**
 * AI Tools Frontend Controller
 * Connects UI to /api/ai endpoints with loading spinners and clean output formatting.
 */

window.AITools = {
  summarize: function(text, outputElem, btnElem) {
    if (!text.trim()) {
      showToast('Please enter text to summarize.', 'error');
      return;
    }

    this._toggleLoading(btnElem, true);
    fetch('/api/ai/summarize', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    })
    .then(res => res.json())
    .then(data => {
      this._toggleLoading(btnElem, false);
      if (data.status === 'success') {
        outputElem.value = data.result;
        showToast('Text summarized successfully!', 'success');
      } else {
        showToast(data.message || 'Error processing request', 'error');
      }
    })
    .catch(err => {
      this._toggleLoading(btnElem, false);
      showToast('Network error while requesting AI service', 'error');
    });
  },

  rewrite: function(text, style, outputElem, btnElem) {
    if (!text.trim()) {
      showToast('Please enter text to rewrite.', 'error');
      return;
    }

    this._toggleLoading(btnElem, true);
    fetch('/api/ai/rewrite', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, style })
    })
    .then(res => res.json())
    .then(data => {
      this._toggleLoading(btnElem, false);
      if (data.status === 'success') {
        outputElem.value = data.result;
        showToast('Text rewritten!', 'success');
      } else {
        showToast(data.message || 'Error processing request', 'error');
      }
    })
    .catch(err => {
      this._toggleLoading(btnElem, false);
      showToast('Network error', 'error');
    });
  },

  explain: function(text, level, outputElem, btnElem) {
    if (!text.trim()) {
      showToast('Please enter topic or code to explain.', 'error');
      return;
    }

    this._toggleLoading(btnElem, true);
    fetch('/api/ai/explain', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, level })
    })
    .then(res => res.json())
    .then(data => {
      this._toggleLoading(btnElem, false);
      if (data.status === 'success') {
        outputElem.innerHTML = escapeHtml(data.result).replace(/\n/g, '<br>');
        showToast('Explanation generated!', 'success');
      } else {
        showToast(data.message || 'Error processing request', 'error');
      }
    })
    .catch(err => {
      this._toggleLoading(btnElem, false);
      showToast('Network error', 'error');
    });
  },

  generateQuestions: function(text, count, outputElem, btnElem) {
    if (!text.trim()) {
      showToast('Please enter text content.', 'error');
      return;
    }

    this._toggleLoading(btnElem, true);
    fetch('/api/ai/questions', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, count })
    })
    .then(res => res.json())
    .then(data => {
      this._toggleLoading(btnElem, false);
      if (data.status === 'success') {
        const questions = data.result;
        outputElem.innerHTML = questions.map(q => `
          <div class="mb-3 p-3 border rounded bg-surface-subtle">
            <div class="fw-bold mb-1">Q${q.number}: ${escapeHtml(q.question)}</div>
            <div class="text-success small"><strong>Answer:</strong> ${escapeHtml(q.answer)}</div>
          </div>
        `).join('');
        showToast('Questions generated!', 'success');
      } else {
        showToast(data.message || 'Error processing request', 'error');
      }
    })
    .catch(err => {
      this._toggleLoading(btnElem, false);
      showToast('Network error', 'error');
    });
  },

  _toggleLoading: function(btn, isLoading) {
    if (!btn) return;
    if (isLoading) {
      btn.disabled = true;
      btn.dataset.origHtml = btn.innerHTML;
      btn.innerHTML = `<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span> Processing...`;
    } else {
      btn.disabled = false;
      if (btn.dataset.origHtml) btn.innerHTML = btn.dataset.origHtml;
    }
  }
};
