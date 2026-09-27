# Contributing to OpenTools

Thank you for your interest in contributing to **OpenTools**! We welcome contributions from developers, designers, writers, and students.

## How to Add a New Tool

OpenTools uses a centralized registry pattern to make adding new tools straightforward:

1. **Add Tool Metadata:**
   Open `tool_registry.py` and append your tool definition to `TOOLS`:
   ```python
   {
       "id": "my-new-tool",
       "name": "My New Tool",
       "category": "developer",
       "description": "Short description of what the tool does",
       "icon": "fa-solid fa-gear",
       "client_side": True,
       "popular": False,
       "featured": False,
       "tags": ["my", "tool", "keywords"],
       "privacy_note": "Processed 100% locally in your browser."
   }
   ```

2. **Add Interactive Widget UI:**
   Add your HTML workspace template inside `templates/tools/_widgets.html` matching `{% elif tool.id == 'my-new-tool' %}`.

3. **Add Client-Side Logic:**
   Add JavaScript logic in `static/js/tools/dev_tools.js` or the appropriate script module.

4. **Run Pytest:**
   Ensure automated tests pass:
   ```bash
   pytest
   ```
