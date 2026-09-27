"""
Centralized Tool Registry for ToolHub.
Every tool available on the platform is defined here with metadata,
categories, search tags, client-side flags, and privacy notices.
"""

CATEGORIES = [
    {
        "id": "developer",
        "name": "Developer Tools",
        "icon": "fa-solid fa-code",
        "description": "Formatters, encoders, decoders, and utilities for software developers.",
        "badge_color": "primary"
    },
    {
        "id": "text",
        "name": "Text Tools",
        "icon": "fa-solid fa-font",
        "description": "Word counting, case converting, diffing, and text formatting tools.",
        "badge_color": "info"
    },
    {
        "id": "calculator",
        "name": "Calculators & Converters",
        "icon": "fa-solid fa-calculator",
        "description": "Scientific calculations, unit conversions, age and date math.",
        "badge_color": "warning"
    },
    {
        "id": "image",
        "name": "Image Tools",
        "icon": "fa-solid fa-image",
        "description": "Browser-based image compression, resizing, cropping, and conversion.",
        "badge_color": "success"
    },
    {
        "id": "pdf",
        "name": "PDF Tools",
        "icon": "fa-solid fa-file-pdf",
        "description": "Merge, split, extract pages, and convert PDF documents locally.",
        "badge_color": "danger"
    },
    {
        "id": "security",
        "name": "Security & Privacy",
        "icon": "fa-solid fa-shield-halved",
        "description": "Password generators, hashers, entropy checkers, and privacy tools.",
        "badge_color": "dark"
    },
    {
        "id": "ai",
        "name": "AI Tools",
        "icon": "fa-solid fa-wand-magic-sparkles",
        "description": "Extensible AI assistants for text summarization, rewriting, and Q&A.",
        "badge_color": "secondary"
    },
    {
        "id": "converter",
        "name": "Data Converters",
        "icon": "fa-solid fa-arrows-rotate",
        "description": "Convert CSV, JSON, Base64, and file data formats quickly.",
        "badge_color": "purple"
    }
]

TOOLS = [
    # --- DEVELOPER TOOLS ---
    {
        "id": "json-formatter",
        "name": "JSON Formatter & Minifier",
        "category": "developer",
        "description": "Format, beautify, minify, and validate JSON data instantly with syntax highlighting.",
        "icon": "fa-brackets-curly",
        "client_side": True,
        "popular": True,
        "featured": True,
        "tags": ["json", "format", "minify", "validate", "beautify", "developer", "parser"],
        "privacy_note": "Processed 100% locally in your browser. No data is sent to external servers."
    },
    {
        "id": "base64-converter",
        "name": "Base64 Encoder / Decoder",
        "category": "developer",
        "description": "Encode text or binary data into Base64 format and decode Base64 strings safely.",
        "icon": "fa-binary",
        "client_side": True,
        "popular": True,
        "featured": False,
        "tags": ["base64", "encode", "decode", "binary", "developer", "string"],
        "privacy_note": "Processed 100% locally in your browser."
    },
    {
        "id": "url-encoder",
        "name": "URL Encoder / Decoder",
        "category": "developer",
        "description": "Encode text for URL query strings or decode percent-encoded URLs.",
        "icon": "fa-link",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["url", "encode", "decode", "uri", "percent", "escape"],
        "privacy_note": "Processed 100% locally in your browser."
    },
    {
        "id": "jwt-decoder",
        "name": "JWT Decoder",
        "category": "developer",
        "description": "Decode JSON Web Tokens (JWT) to inspect header, payload claims, and signature info.",
        "icon": "fa-key",
        "client_side": True,
        "popular": True,
        "featured": True,
        "tags": ["jwt", "token", "decode", "oauth", "auth", "claims", "bearer"],
        "privacy_note": "Your secrets and tokens never leave your browser. Decoded locally."
    },
    {
        "id": "uuid-generator",
        "name": "UUID / GUID Generator",
        "category": "developer",
        "description": "Generate bulk cryptographically secure RFC 4122 v4 and v1 UUIDs/GUIDs.",
        "icon": "fa-fingerprint",
        "client_side": True,
        "popular": True,
        "featured": False,
        "tags": ["uuid", "guid", "generator", "unique", "id", "random", "rfc4122"],
        "privacy_note": "Generated locally using Web Crypto API."
    },
    {
        "id": "regex-tester",
        "name": "Regex Tester & Matcher",
        "category": "developer",
        "description": "Test JavaScript regular expressions in real-time with pattern syntax highlighting and match groups.",
        "icon": "fa-asterisk",
        "client_side": True,
        "popular": True,
        "featured": False,
        "tags": ["regex", "regexp", "regular expression", "test", "match", "replace"],
        "privacy_note": "Executed locally using browser JavaScript engine."
    },
    {
        "id": "timestamp-converter",
        "name": "Unix Timestamp Converter",
        "category": "developer",
        "description": "Convert Unix epoch timestamps (seconds/milliseconds) to human-readable dates and back.",
        "icon": "fa-clock",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["timestamp", "unix", "epoch", "time", "date", "iso8601", "utc"],
        "privacy_note": "Calculated locally."
    },
    {
        "id": "color-converter",
        "name": "Color Code Converter",
        "category": "developer",
        "description": "Convert color formats between HEX, RGB, HSL, and HSV with live visual preview.",
        "icon": "fa-palette",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["color", "hex", "rgb", "hsl", "hsv", "css", "palette", "picker"],
        "privacy_note": "Processed 100% locally in your browser."
    },
    {
        "id": "html-formatter",
        "name": "HTML Formatter & Minifier",
        "category": "developer",
        "description": "Clean up, format, indent, or compress raw HTML markup.",
        "icon": "fa-code",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["html", "format", "beautify", "minify", "markup", "web"],
        "privacy_note": "Processed locally."
    },
    {
        "id": "css-formatter",
        "name": "CSS Formatter & Minifier",
        "category": "developer",
        "description": "Format, beautify, or minify CSS stylesheets for optimal web loading.",
        "icon": "fa-css3-alt",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["css", "format", "beautify", "minify", "styles", "stylesheet"],
        "privacy_note": "Processed locally."
    },
    {
        "id": "js-formatter",
        "name": "JavaScript Formatter",
        "category": "developer",
        "description": "Format, beautify, or minify JavaScript code snippets cleanly.",
        "icon": "fa-square-js",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["js", "javascript", "format", "beautify", "minify", "code"],
        "privacy_note": "Processed locally."
    },
    {
        "id": "markdown-preview",
        "name": "Markdown Live Editor",
        "category": "developer",
        "description": "Write Markdown text with instant side-by-side rendered HTML preview, download, and copy.",
        "icon": "fa-file-lines",
        "client_side": True,
        "popular": True,
        "featured": False,
        "tags": ["markdown", "md", "preview", "editor", "gfm", "render"],
        "privacy_note": "Rendered 100% locally in your browser."
    },
    {
        "id": "sql-formatter",
        "name": "SQL Query Formatter",
        "category": "developer",
        "description": "Beautify and format complex SQL queries with proper keyword capitalization and line indents.",
        "icon": "fa-database",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["sql", "query", "format", "beautify", "database", "postgres", "mysql"],
        "privacy_note": "Processed locally."
    },

    # --- TEXT TOOLS ---
    {
        "id": "word-counter",
        "name": "Word & Character Counter",
        "category": "text",
        "description": "Count words, total characters, characters without spaces, sentences, paragraphs, and reading time.",
        "icon": "fa-calculator",
        "client_side": True,
        "popular": True,
        "featured": True,
        "tags": ["word", "counter", "character", "sentence", "paragraph", "reading time", "text"],
        "privacy_note": "Analyzed locally in your browser."
    },
    {
        "id": "case-converter",
        "name": "Text Case Converter",
        "category": "text",
        "description": "Transform text to UPPERCASE, lowercase, Title Case, Sentence case, camelCase, PascalCase, snake_case, and kebab-case.",
        "icon": "fa-text-height",
        "client_side": True,
        "popular": True,
        "featured": False,
        "tags": ["case", "uppercase", "lowercase", "titlecase", "camelcase", "snake_case", "kebab-case"],
        "privacy_note": "Processed locally."
    },
    {
        "id": "remove-duplicate-lines",
        "name": "Remove Duplicate Lines",
        "category": "text",
        "description": "Clean list data by removing duplicate lines, trimming whitespace, or preserving line order.",
        "icon": "fa-filter",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["duplicate", "lines", "remove", "dedupe", "text", "list", "clean"],
        "privacy_note": "Processed locally."
    },
    {
        "id": "sort-lines",
        "name": "Sort Text Lines",
        "category": "text",
        "description": "Sort lines alphabetically (A-Z, Z-A), numerically, or by line length.",
        "icon": "fa-arrow-down-a-z",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["sort", "lines", "alphabetical", "order", "numerical", "text"],
        "privacy_note": "Processed locally."
    },
    {
        "id": "find-replace",
        "name": "Find & Replace Text",
        "category": "text",
        "description": "Find words or phrases in large text blocks and replace them using plain text or regex.",
        "icon": "fa-magnifying-glass-arrow-right",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["find", "replace", "text", "search", "substitute", "regex"],
        "privacy_note": "Processed locally."
    },
    {
        "id": "text-diff",
        "name": "Text Diff Checker",
        "category": "text",
        "description": "Compare two blocks of text side-by-side or inline to visually highlight additions, deletions, and changes.",
        "icon": "fa-code-compare",
        "client_side": True,
        "popular": True,
        "featured": True,
        "tags": ["diff", "compare", "text", "changes", "difference", "side-by-side"],
        "privacy_note": "Compared 100% locally in your browser."
    },
    {
        "id": "lorem-generator",
        "name": "Lorem Ipsum Generator",
        "category": "text",
        "description": "Generate custom placeholder text in paragraphs, sentences, or words for layout designs.",
        "icon": "fa-align-left",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["lorem", "ipsum", "placeholder", "generator", "dummy", "text"],
        "privacy_note": "Generated locally."
    },

    # --- CALCULATOR TOOLS ---
    {
        "id": "scientific-calculator",
        "name": "Scientific Calculator",
        "category": "calculator",
        "description": "Advanced scientific calculator supporting trigonometry, exponents, roots, logarithms, and memory functions.",
        "icon": "fa-calculator",
        "client_side": True,
        "popular": True,
        "featured": True,
        "tags": ["calculator", "scientific", "math", "sin", "cos", "log", "power", "square root"],
        "privacy_note": "Calculations happen in browser memory."
    },
    {
        "id": "unit-converter",
        "name": "Universal Unit Converter",
        "category": "calculator",
        "description": "Convert Length, Weight, Temperature, Area, Volume, Speed, Time, Data Storage, Energy, and Pressure.",
        "icon": "fa-ruler-combined",
        "client_side": True,
        "popular": True,
        "featured": False,
        "tags": ["unit", "converter", "length", "weight", "temperature", "volume", "speed", "data"],
        "privacy_note": "Calculated locally."
    },
    {
        "id": "percentage-calculator",
        "name": "Percentage Calculator",
        "category": "calculator",
        "description": "Calculate percentage values, percentage increases/decreases, and what percent one number is of another.",
        "icon": "fa-percent",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["percentage", "percent", "math", "calculator", "increase", "decrease"],
        "privacy_note": "Calculated locally."
    },
    {
        "id": "age-calculator",
        "name": "Age Calculator",
        "category": "calculator",
        "description": "Calculate exact age in years, months, weeks, days, hours, and minutes from birthdate.",
        "icon": "fa-cake-candles",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["age", "calculator", "birthday", "years", "months", "days", "date"],
        "privacy_note": "Personal birthdates are calculated locally and never transmitted."
    },
    {
        "id": "date-difference",
        "name": "Date Difference Calculator",
        "category": "calculator",
        "description": "Calculate the exact duration, working days, or total days between two dates.",
        "icon": "fa-calendar-days",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["date", "difference", "duration", "days", "calendar", "calculator"],
        "privacy_note": "Calculated locally."
    },
    {
        "id": "bmi-calculator",
        "name": "BMI Calculator",
        "category": "calculator",
        "description": "Calculate Body Mass Index (BMI) using Metric or Imperial measurements with health category ranges.",
        "icon": "fa-weight-scale",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["bmi", "health", "body mass index", "weight", "height", "fitness"],
        "privacy_note": "No medical or personal data is collected or stored."
    },

    # --- IMAGE TOOLS ---
    {
        "id": "image-compressor",
        "name": "Image Compressor",
        "category": "image",
        "description": "Compress JPEG, PNG, and WebP images locally to reduce file size while maintaining visual quality.",
        "icon": "fa-file-image",
        "client_side": True,
        "popular": True,
        "featured": True,
        "tags": ["image", "compress", "optimize", "jpeg", "png", "webp", "file size"],
        "privacy_note": "Your images are compressed 100% locally in your browser using HTML5 Canvas. Never uploaded."
    },
    {
        "id": "image-resizer",
        "name": "Image Resizer",
        "category": "image",
        "description": "Resize image dimensions by pixels or percentage with aspect ratio lock.",
        "icon": "fa-expand",
        "client_side": True,
        "popular": True,
        "featured": False,
        "tags": ["image", "resize", "dimensions", "width", "height", "scale", "pixels"],
        "privacy_note": "Processed 100% locally in browser."
    },
    {
        "id": "image-converter",
        "name": "Image Format Converter",
        "category": "image",
        "description": "Convert images between PNG, JPG/JPEG, and WebP formats instantly.",
        "icon": "fa-repeat",
        "client_side": True,
        "popular": True,
        "featured": False,
        "tags": ["image", "convert", "png", "jpg", "jpeg", "webp", "format"],
        "privacy_note": "Converted locally inside your browser."
    },
    {
        "id": "image-cropper",
        "name": "Image Cropper",
        "category": "image",
        "description": "Crop images with interactive selection box and aspect ratio presets.",
        "icon": "fa-crop-simple",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["image", "crop", "trim", "aspect ratio", "editor", "picture"],
        "privacy_note": "Cropped locally in your browser."
    },
    {
        "id": "image-metadata",
        "name": "Image Metadata / EXIF Viewer",
        "category": "image",
        "description": "View camera settings, date taken, dimensions, and hidden EXIF metadata embedded in images.",
        "icon": "fa-circle-info",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["image", "exif", "metadata", "camera", "photo", "location", "privacy"],
        "privacy_note": "Metadata is read strictly in your browser. Warns about hidden location coordinates."
    },

    # --- PDF TOOLS ---
    {
        "id": "pdf-to-images",
        "name": "PDF to Images Converter",
        "category": "pdf",
        "description": "Convert PDF document pages into high-resolution PNG or JPEG images.",
        "icon": "fa-file-picture",
        "client_side": True,
        "popular": True,
        "featured": True,
        "tags": ["pdf", "images", "convert", "png", "jpeg", "pages", "extract"],
        "privacy_note": "PDF pages are rendered locally using PDF.js. Your document remains private."
    },
    {
        "id": "images-to-pdf",
        "name": "Images to PDF Converter",
        "category": "pdf",
        "description": "Combine multiple images into a single clean PDF document.",
        "icon": "fa-file-export",
        "client_side": True,
        "popular": True,
        "featured": False,
        "tags": ["images", "pdf", "convert", "combine", "document", "create"],
        "privacy_note": "PDF compiled locally in your browser."
    },
    {
        "id": "pdf-merge",
        "name": "PDF Merger",
        "category": "pdf",
        "description": "Merge multiple PDF files into one ordered PDF document.",
        "icon": "fa-object-group",
        "client_side": True,
        "popular": True,
        "featured": True,
        "tags": ["pdf", "merge", "combine", "join", "files", "document"],
        "privacy_note": "PDFs are merged directly inside your web browser using WebAssembly / PDF-Lib."
    },
    {
        "id": "pdf-split",
        "name": "PDF Splitter",
        "category": "pdf",
        "description": "Split a multi-page PDF into separate single-page PDF files.",
        "icon": "fa-scissors",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["pdf", "split", "divide", "pages", "separate"],
        "privacy_note": "Processed 100% locally in browser."
    },
    {
        "id": "pdf-extractor",
        "name": "PDF Page Extractor",
        "category": "pdf",
        "description": "Extract specific page numbers or ranges from a PDF into a new PDF document.",
        "icon": "fa-file-circle-plus",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["pdf", "extract", "pages", "select", "download"],
        "privacy_note": "Extracted locally."
    },
    {
        "id": "pdf-metadata",
        "name": "PDF Metadata Viewer",
        "category": "pdf",
        "description": "Inspect PDF author, producer, title, subject, page count, and creation date.",
        "icon": "fa-circle-info",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["pdf", "metadata", "info", "properties", "author", "pages"],
        "privacy_note": "Read locally in browser."
    },

    # --- SECURITY & PRIVACY TOOLS ---
    {
        "id": "password-generator",
        "name": "Password & Passphrase Generator",
        "category": "security",
        "description": "Generate ultra-secure, cryptographically strong random passwords or passphrase strings.",
        "icon": "fa-shield-cat",
        "client_side": True,
        "popular": True,
        "featured": True,
        "tags": ["password", "generator", "security", "random", "passphrase", "strong", "crypto"],
        "privacy_note": "Passwords are generated strictly in your browser using window.crypto. NEVER saved or logged."
    },
    {
        "id": "password-checker",
        "name": "Password Strength Analyzer",
        "category": "security",
        "description": "Evaluate password strength, entropy bits, estimated crack time, and weakness alerts.",
        "icon": "fa-lock-open",
        "client_side": True,
        "popular": True,
        "featured": False,
        "tags": ["password", "strength", "checker", "entropy", "security", "crack time"],
        "privacy_note": "Evaluated 100% locally. Passwords are never transmitted anywhere."
    },
    {
        "id": "hash-generator",
        "name": "Text Hash Generator",
        "category": "security",
        "description": "Compute SHA-256, SHA-512, SHA-1, and MD5 cryptographic hashes for any text string.",
        "icon": "fa-hashtag",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["hash", "sha256", "sha512", "md5", "crypto", "checksum", "digest"],
        "privacy_note": "Computed using browser Web Crypto API. Clarification: Hashing is one-way, not encryption."
    },
    {
        "id": "file-hash",
        "name": "Local File Checksum Calculator",
        "category": "security",
        "description": "Calculate SHA-256 or MD5 hashes for large local files to verify integrity and downloads.",
        "icon": "fa-file-shield",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["file", "hash", "checksum", "sha256", "integrity", "verify"],
        "privacy_note": "Files are read in chunks locally via Web FileReader. Zero bytes uploaded."
    },
    {
        "id": "url-safety",
        "name": "URL & Domain Technical Inspector",
        "category": "security",
        "description": "Perform technical analysis of URL structure, protocol, parameters, and potential phishing indicators.",
        "icon": "fa-shield-virus",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["url", "safety", "security", "phishing", "domain", "inspector", "links"],
        "privacy_note": "Performs static technical analysis locally. Clearly marks heuristic indicators vs verified reputation."
    },

    # --- AI TOOLS ---
    {
        "id": "ai-summarizer",
        "name": "AI Text Summarizer",
        "category": "ai",
        "description": "Summarize long articles, documents, or reports into bullet points or concise key takeaways.",
        "icon": "fa-wand-magic-sparkles",
        "client_side": False,
        "popular": True,
        "featured": True,
        "tags": ["ai", "summarize", "summary", "text", "article", "extensible"],
        "privacy_note": "Extensible AI pipeline with fallback rule engine if external API key is unconfigured."
    },
    {
        "id": "ai-rewriter",
        "name": "AI Text Rewriter & Paraphraser",
        "category": "ai",
        "description": "Rewrite text to improve clarity, tone, conciseness, or change vocabulary.",
        "icon": "fa-pen-sparkles",
        "client_side": False,
        "popular": False,
        "featured": False,
        "tags": ["ai", "rewrite", "paraphrase", "clarity", "grammar", "tone"],
        "privacy_note": "Extensible AI service architecture."
    },
    {
        "id": "ai-explainer",
        "name": "AI Text Explainer",
        "category": "ai",
        "description": "Explain complex topics, code snippets, or jargon in simple layman terms.",
        "icon": "fa-brain",
        "client_side": False,
        "popular": False,
        "featured": False,
        "tags": ["ai", "explain", "learn", "simplifier", "education", "code"],
        "privacy_note": "Extensible AI service architecture."
    },
    {
        "id": "ai-question-generator",
        "name": "AI Question & Quiz Generator",
        "category": "ai",
        "description": "Generate comprehension questions or flashcards from provided study text.",
        "icon": "fa-circle-question",
        "client_side": False,
        "popular": False,
        "featured": False,
        "tags": ["ai", "questions", "quiz", "flashcards", "study", "education"],
        "privacy_note": "Extensible AI service architecture."
    },

    # --- CONVERTER TOOLS ---
    {
        "id": "csv-to-json",
        "name": "CSV to JSON / JSON to CSV",
        "category": "converter",
        "description": "Convert tabular CSV data to structured JSON objects and vice versa with custom delimiters.",
        "icon": "fa-file-csv",
        "client_side": True,
        "popular": True,
        "featured": False,
        "tags": ["csv", "json", "convert", "table", "excel", "data", "parser"],
        "privacy_note": "Converted locally in your browser."
    },
    {
        "id": "base64-file",
        "name": "File to Base64 Data URI",
        "category": "converter",
        "description": "Convert images, fonts, or files into Data URI strings for HTML/CSS embedding.",
        "icon": "fa-file-code",
        "client_side": True,
        "popular": False,
        "featured": False,
        "tags": ["file", "base64", "data uri", "embed", "css", "html"],
        "privacy_note": "Processed 100% locally."
    }
]

# Quick access helpers
TOOLS_BY_ID = {t["id"]: t for t in TOOLS}
CATEGORIES_BY_ID = {c["id"]: c for c in CATEGORIES}

def get_all_tools():
    return TOOLS

def get_all_categories():
    return CATEGORIES

def get_tool_by_id(tool_id):
    return TOOLS_BY_ID.get(tool_id)

def get_category_by_id(category_id):
    return CATEGORIES_BY_ID.get(category_id)

def get_tools_by_category(category_id):
    return [t for t in TOOLS if t["category"] == category_id]

def get_popular_tools():
    return [t for t in TOOLS if t.get("popular", False)]

def get_featured_tools():
    return [t for t in TOOLS if t.get("featured", False)]

def search_tools(query):
    if not query:
        return TOOLS
    q = query.strip().lower()
    results = []
    for tool in TOOLS:
        score = 0
        if q in tool["name"].lower():
            score += 10
        if q in tool["description"].lower():
            score += 3
        if q in tool["category"].lower():
            score += 5
        for tag in tool.get("tags", []):
            if q in tag.lower():
                score += 4
        if score > 0:
            results.append((score, tool))
    results.sort(key=lambda x: x[0], reverse=True)
    return [item[1] for item in results]
