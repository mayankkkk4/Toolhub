from flask import Blueprint, render_template, abort
from tool_registry import get_tool_by_id, get_category_by_id, get_tools_by_category, get_all_tools

tools_bp = Blueprint('tools', __name__)

@tools_bp.route('/tools/<tool_id>')
def tool_detail(tool_id):
    tool = get_tool_by_id(tool_id)
    if not tool:
        abort(404)
    
    category = get_category_by_id(tool['category'])
    related_tools = [t for t in get_tools_by_category(tool['category']) if t['id'] != tool_id][:4]
    
    return render_template(
        'tool_detail.html',
        tool=tool,
        category=category,
        related_tools=related_tools
    )
