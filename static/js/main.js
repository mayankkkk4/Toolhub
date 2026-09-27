/**
 * ToolHub Global JavaScript Core
 * Handles Theme Toggling, Global Tool Search, Recently Used Tools, and Toast Notifications
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initGlobalSearch();
  initRecentlyUsedTools();
  initPWAInstall();
});

// --- 1. Theme Management ---
function initTheme() {
  const themeToggleBtn = document.getElementById('theme-toggle-btn');
  const storedTheme = localStorage.getItem('toolhub_theme') || 
    (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    
  setTheme(storedTheme);

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';
      setTheme(newTheme);
    });
  }
}

function setTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('toolhub_theme', theme);
  const icon = document.getElementById('theme-toggle-icon');
  if (icon) {
    icon.className = theme === 'dark' ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
  }
}

// --- 2. Global Instant Tool Search ---
function initGlobalSearch() {
  const searchInput = document.getElementById('global-tool-search');
  const searchDropdown = document.getElementById('search-dropdown-results');
  
  if (!searchInput || !searchDropdown) return;

  let debounceTimer;

  searchInput.addEventListener('input', (e) => {
    clearTimeout(debounceTimer);
    const query = e.target.value.trim();

    if (query.length < 1) {
      searchDropdown.classList.remove('active');
      searchDropdown.innerHTML = '';
      return;
    }

    debounceTimer = setTimeout(() => {
      fetch(`/api/tools?search=${encodeURIComponent(query)}`)
        .then(res => res.json())
        .then(data => {
          if (data.status === 'success' && data.tools.length > 0) {
            searchDropdown.innerHTML = data.tools.map(tool => `
              <a href="/tools/${tool.id}" class="search-dropdown-item" onclick="trackRecentTool('${tool.id}')">
                <div class="search-dropdown-icon">
                  <i class="${tool.icon || 'fa-solid fa-wrench'}"></i>
                </div>
                <div>
                  <div class="fw-bold">${escapeHtml(tool.name)}</div>
                  <div class="text-muted small">${escapeHtml(tool.description)}</div>
                </div>
              </a>
            `).join('');
            searchDropdown.classList.add('active');
          } else {
            searchDropdown.innerHTML = `
              <div class="p-3 text-center text-muted small">
                No tools found for "<strong class="text-primary">${escapeHtml(query)}</strong>"
              </div>
            `;
            searchDropdown.classList.add('active');
          }
        })
        .catch(err => console.error('Search error:', err));
    }, 150);
  });

  // Close search dropdown on click outside
  document.addEventListener('click', (e) => {
    if (!searchInput.contains(e.target) && !searchDropdown.contains(e.target)) {
      searchDropdown.classList.remove('active');
    }
  });
}

// --- 3. Recently Used Tools (localStorage) ---
function trackRecentTool(toolId) {
  let recents = JSON.parse(localStorage.getItem('toolhub_recent') || '[]');
  recents = recents.filter(id => id !== toolId);
  recents.unshift(toolId);
  if (recents.length > 8) recents.pop();
  localStorage.setItem('toolhub_recent', JSON.stringify(recents));
}

function initRecentlyUsedTools() {
  const recentContainer = document.getElementById('recently-used-tools-container');
  if (!recentContainer) return;

  const recents = JSON.parse(localStorage.getItem('toolhub_recent') || '[]');
  if (recents.length === 0) {
    recentContainer.innerHTML = `<div class="col-12 text-muted small text-center">No recently used tools yet.</div>`;
    return;
  }

  fetch('/api/tools')
    .then(res => res.json())
    .then(data => {
      if (data.status === 'success') {
        const toolMap = {};
        data.tools.forEach(t => toolMap[t.id] = t);

        const items = recents.map(id => toolMap[id]).filter(Boolean);
        if (items.length > 0) {
          recentContainer.innerHTML = items.map(tool => `
            <div class="col-md-4 col-lg-3 mb-3">
              <a href="/tools/${tool.id}" class="tool-card text-decoration-none" onclick="trackRecentTool('${tool.id}')">
                <div class="tool-card-icon"><i class="${tool.icon}"></i></div>
                <div class="tool-card-title">${escapeHtml(tool.name)}</div>
                <div class="tool-card-desc">${escapeHtml(tool.description)}</div>
              </a>
            </div>
          `).join('');
        }
      }
    });
}

// --- 4. Toast Notification Utility ---
function showToast(message, type = 'success') {
  const toastContainer = document.getElementById('toast-container');
  if (!toastContainer) return;

  const toastId = 'toast-' + Date.now();
  const bgClass = type === 'success' ? 'bg-success text-white' : type === 'error' ? 'bg-danger text-white' : 'bg-dark text-white';

  const html = `
    <div id="${toastId}" class="toast align-items-center ${bgClass} border-0 show" role="alert" aria-live="assertive" aria-atomic="true">
      <div class="d-flex">
        <div class="toast-body d-flex align-items-center gap-2">
          <i class="${type === 'success' ? 'fa-solid fa-circle-check' : 'fa-solid fa-circle-exclamation'}"></i>
          ${escapeHtml(message)}
        </div>
        <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
      </div>
    </div>
  `;

  toastContainer.insertAdjacentHTML('beforeend', html);
  setTimeout(() => {
    const elem = document.getElementById(toastId);
    if (elem) elem.remove();
  }, 3500);
}

// Helper: Copy Text to Clipboard
function copyToClipboard(text, successMessage = 'Copied to clipboard!') {
  if (!text) {
    showToast('Nothing to copy!', 'error');
    return;
  }
  navigator.clipboard.writeText(text)
    .then(() => showToast(successMessage, 'success'))
    .catch(() => showToast('Failed to copy', 'error'));
}

// Helper: Download File
function downloadFile(filename, content, mimeType = 'text/plain') {
  const blob = new Blob([content], { type: mimeType });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
  showToast(`Downloaded ${filename}`, 'success');
}

// Helper: Escape HTML
function escapeHtml(str) {
  return String(str).replace(/[&<>"']/g, function(m) {
    return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' }[m];
  });
}

// --- 5. PWA Install Prompt Handler ---
let deferredPwaPrompt;
function initPWAInstall() {
  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPwaPrompt = e;
    const banner = document.getElementById('pwa-install-banner');
    if (banner) banner.classList.remove('d-none');
  });

  const installBtn = document.getElementById('pwa-install-btn');
  if (installBtn) {
    installBtn.addEventListener('click', () => {
      if (deferredPwaPrompt) {
        deferredPwaPrompt.prompt();
        deferredPwaPrompt.userChoice.then((choiceResult) => {
          if (choiceResult.outcome === 'accepted') {
            showToast('ToolHub installed successfully!', 'success');
          }
          deferredPwaPrompt = null;
          const banner = document.getElementById('pwa-install-banner');
          if (banner) banner.classList.add('d-none');
        });
      }
    });
  }
}
