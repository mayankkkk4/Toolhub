const CACHE_NAME = 'toolhub-v1.0';
const ASSETS_TO_CACHE = [
  '/',
  '/tools',
  '/static/css/main.css',
  '/static/css/tools.css',
  '/static/js/main.js',
  '/static/js/favorites.js',
  '/static/js/tools/dev_tools.js',
  '/static/js/tools/text_tools.js',
  '/static/js/tools/calc_tools.js',
  '/static/js/tools/image_tools.js',
  '/static/js/tools/sec_tools.js'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request).then((response) => {
      return response || fetch(e.request);
    })
  );
});
