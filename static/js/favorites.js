/**
 * ToolHub Favorites Manager
 * Supports anonymous localStorage favorites and server DB sync
 */

document.addEventListener('DOMContentLoaded', () => {
  initFavoritesUI();
});

function getLocalFavorites() {
  return JSON.parse(localStorage.getItem('toolhub_favs') || '[]');
}

function setLocalFavorites(favs) {
  localStorage.setItem('toolhub_favs', JSON.stringify(favs));
}

function toggleFavorite(toolId, buttonElem) {
  fetch('/api/favorites', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ tool_id: toolId })
  })
  .then(res => {
    if (res.status === 401) {
      // Anonymous user fallback to localStorage
      let favs = getLocalFavorites();
      let added = false;
      if (favs.includes(toolId)) {
        favs = favs.filter(id => id !== toolId);
      } else {
        favs.push(toolId);
        added = true;
      }
      setLocalFavorites(favs);
      updateFavButtonState(buttonElem, added);
      showToast(added ? 'Added to favorites!' : 'Removed from favorites.', 'info');
      return null;
    }
    return res.json();
  })
  .then(data => {
    if (data && data.status === 'success') {
      const added = data.action === 'added';
      updateFavButtonState(buttonElem, added);
      showToast(added ? 'Saved to your account favorites!' : 'Removed from favorites.', 'success');
    }
  });
}

function updateFavButtonState(btn, isFav) {
  if (!btn) return;
  const icon = btn.querySelector('i');
  if (isFav) {
    btn.classList.add('text-warning');
    if (icon) icon.className = 'fa-solid fa-star';
  } else {
    btn.classList.remove('text-warning');
    if (icon) icon.className = 'fa-regular fa-star';
  }
}

function initFavoritesUI() {
  const favBtns = document.querySelectorAll('.btn-fav-toggle');
  if (favBtns.length === 0) return;

  fetch('/api/favorites')
    .then(res => res.json())
    .then(data => {
      let activeFavs = [];
      if (data.status === 'success' && data.favorites.length > 0) {
        activeFavs = data.favorites;
      } else {
        activeFavs = getLocalFavorites();
      }

      favBtns.forEach(btn => {
        const toolId = btn.getAttribute('data-tool-id');
        if (activeFavs.includes(toolId)) {
          updateFavButtonState(btn, true);
        }
        btn.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          toggleFavorite(toolId, btn);
        });
      });
    });
}
