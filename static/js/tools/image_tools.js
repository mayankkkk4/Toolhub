/**
 * Image Tools Implementation Module
 * Processed 100% locally in the browser using HTML5 Canvas and FileReader APIs.
 */

window.ImageTools = {
  // 1. Image Compressor
  compressImage: function(file, quality = 0.8, format = 'image/jpeg', callback) {
    if (!file) return;
    const reader = new FileReader();
    reader.onload = function(e) {
      const img = new Image();
      img.onload = function() {
        const canvas = document.createElement('canvas');
        canvas.width = img.width;
        canvas.height = img.height;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(img, 0, 0);

        canvas.toBlob(function(blob) {
          const compressedUrl = URL.createObjectURL(blob);
          callback({
            originalSize: file.size,
            compressedSize: blob.size,
            compressedUrl: compressedUrl,
            blob: blob,
            width: img.width,
            height: img.height
          });
        }, format, quality);
      };
      img.src = e.target.result;
    };
    reader.readAsDataURL(file);
  },

  // 2. Image Resizer
  resizeImage: function(file, newWidth, newHeight, maintainAspect = true, callback) {
    if (!file) return;
    const reader = new FileReader();
    reader.onload = function(e) {
      const img = new Image();
      img.onload = function() {
        let targetW = newWidth ? parseInt(newWidth) : img.width;
        let targetH = newHeight ? parseInt(newHeight) : img.height;

        if (maintainAspect) {
          if (newWidth && !newHeight) {
            targetH = Math.round(img.height * (targetW / img.width));
          } else if (newHeight && !newWidth) {
            targetW = Math.round(img.width * (targetH / img.height));
          }
        }

        const canvas = document.createElement('canvas');
        canvas.width = targetW;
        canvas.height = targetH;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(img, 0, 0, targetW, targetH);

        canvas.toBlob(function(blob) {
          const url = URL.createObjectURL(blob);
          callback({
            url: url,
            blob: blob,
            width: targetW,
            height: targetH,
            size: blob.size
          });
        }, file.type || 'image/png');
      };
      img.src = e.target.result;
    };
    reader.readAsDataURL(file);
  },

  // 3. Image Format Converter
  convertFormat: function(file, targetMime = 'image/webp', callback) {
    if (!file) return;
    const reader = new FileReader();
    reader.onload = function(e) {
      const img = new Image();
      img.onload = function() {
        const canvas = document.createElement('canvas');
        canvas.width = img.width;
        canvas.height = img.height;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(img, 0, 0);

        canvas.toBlob(function(blob) {
          const url = URL.createObjectURL(blob);
          callback({
            url: url,
            blob: blob,
            size: blob.size,
            mime: targetMime
          });
        }, targetMime, 0.92);
      };
      img.src = e.target.result;
    };
    reader.readAsDataURL(file);
  },

  // 4. Image Metadata Reader (Local FileReader inspects header bytes)
  readImageMetadata: function(file, callback) {
    if (!file) return;
    const reader = new FileReader();
    reader.onload = function(e) {
      const img = new Image();
      img.onload = function() {
        const meta = {
          fileName: file.name,
          fileSize: (file.size / 1024).toFixed(2) + ' KB',
          mimeType: file.type,
          width: img.width,
          height: img.height,
          aspectRatio: (img.width / img.height).toFixed(2),
          lastModified: new Date(file.lastModified).toLocaleString(),
          privacyWarning: "Note: Images taken with smartphones or GPS cameras often embed EXIF location data. Use OpenTools to verify or strip metadata before sharing online."
        };
        callback(meta);
      };
      img.src = e.target.result;
    };
    reader.readAsDataURL(file);
  }
};
