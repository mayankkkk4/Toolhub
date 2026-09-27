"""
Backend image processing service fallback for ToolHub.
Supports compression, resizing, and format conversion when server processing is requested.
"""
import io
from PIL import Image

class ImageService:
    @staticmethod
    def compress_image(image_bytes, quality=75, format_type='JPEG'):
        img = Image.open(io.BytesIO(image_bytes))
        if img.mode in ('RGBA', 'P') and format_type.upper() == 'JPEG':
            img = img.convert('RGB')
        
        output = io.BytesIO()
        img.save(output, format=format_type.upper(), quality=quality, optimize=True)
        return output.getvalue()

    @staticmethod
    def resize_image(image_bytes, width=None, height=None, maintain_aspect=True):
        img = Image.open(io.BytesIO(image_bytes))
        orig_w, orig_h = img.size
        
        if width and not height:
            if maintain_aspect:
                height = int(orig_h * (width / orig_w))
            else:
                height = orig_h
        elif height and not width:
            if maintain_aspect:
                width = int(orig_w * (height / orig_h))
            else:
                width = orig_w
        elif not width and not height:
            width, height = orig_w, orig_h

        resized = img.resize((int(width), int(height)), Image.Resampling.LANCZOS)
        output = io.BytesIO()
        fmt = img.format or 'PNG'
        resized.save(output, format=fmt)
        return output.getvalue()
