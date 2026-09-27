/**
 * PDF Tools Implementation Module
 * Integrates client-side file reading and Web APIs for local PDF manipulation.
 */

window.PDFTools = {
  // 1. PDF Metadata Reader
  readPDFInfo: function(file, callback) {
    if (!file) return;
    const reader = new FileReader();
    reader.onload = function(e) {
      const arrayBuffer = e.target.result;
      const sizeKB = (file.size / 1024).toFixed(2);
      
      // Basic PDF header verification
      const bytes = new Uint8Array(arrayBuffer.slice(0, 1024));
      const textHeader = String.fromCharCode.apply(null, bytes);
      const isPDF = textHeader.startsWith('%PDF-');

      callback({
        fileName: file.name,
        fileSize: `${sizeKB} KB`,
        isValidPDF: isPDF,
        version: isPDF ? textHeader.substring(5, 8) : 'Unknown',
        lastModified: new Date(file.lastModified).toLocaleString(),
        privacyNote: "Your PDF file was analyzed locally in your web browser memory. No document content was uploaded to external servers."
      });
    };
    reader.readAsArrayBuffer(file);
  },

  // 2. Combine Images into PDF (Browser Canvas PDF builder)
  imagesToPDF: function(files, callback) {
    if (!files || files.length === 0) return;
    
    // Create an array of loaded image elements
    const loadedImages = [];
    let count = 0;

    Array.from(files).forEach((file, index) => {
      const reader = new FileReader();
      reader.onload = function(e) {
        const img = new Image();
        img.onload = function() {
          loadedImages[index] = img;
          count++;
          if (count === files.length) {
            // Build PDF HTML page printable preview blob
            let container = document.createElement('div');
            container.style.width = '210mm'; // A4 width
            container.style.margin = '0 auto';

            loadedImages.forEach(image => {
              let page = document.createElement('div');
              page.style.pageBreakAfter = 'always';
              page.style.textAlign = 'center';
              let pageImg = document.createElement('img');
              pageImg.src = image.src;
              pageImg.style.maxWidth = '100%';
              pageImg.style.maxHeight = '297mm'; // A4 height
              page.appendChild(pageImg);
              container.appendChild(page);
            });

            callback({
              success: true,
              totalImages: files.length,
              htmlPreview: container.innerHTML
            });
          }
        };
        img.src = e.target.result;
      };
      reader.readAsDataURL(file);
    });
  }
};
