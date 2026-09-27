from flask import Blueprint, request, jsonify, session
from tool_registry import (
    get_all_tools, get_tool_by_id, get_all_categories,
    get_category_by_id, get_tools_by_category, search_tools
)
from services import ai_service
from models import db, Favorite, Feedback, ToolStat

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/tools', methods=['GET'])
def get_tools():
    query = request.args.get('search', '').strip()
    category = request.args.get('category', '').strip()
    
    if query:
        tools = search_tools(query)
    elif category:
        tools = get_tools_by_category(category)
    else:
        tools = get_all_tools()
        
    return jsonify({
        'status': 'success',
        'count': len(tools),
        'tools': tools
    })

@api_bp.route('/tools/<tool_id>', methods=['GET'])
def get_tool(tool_id):
    tool = get_tool_by_id(tool_id)
    if not tool:
        return jsonify({'status': 'error', 'message': 'Tool not found'}), 404
    return jsonify({'status': 'success', 'tool': tool})

@api_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = get_all_categories()
    return jsonify({'status': 'success', 'categories': categories})

@api_bp.route('/tools/stat', methods=['POST'])
def record_stat():
    data = request.get_json() or {}
    tool_id = data.get('tool_id')
    if not tool_id or not get_tool_by_id(tool_id):
        return jsonify({'status': 'error', 'message': 'Invalid tool_id'}), 400
        
    stat = ToolStat.query.filter_by(tool_id=tool_id).first()
    if not stat:
        stat = ToolStat(tool_id=tool_id, use_count=1)
        db.session.add(stat)
    else:
        stat.use_count += 1
    db.session.commit()
    
    return jsonify({'status': 'success', 'use_count': stat.use_count})

# --- AI ENDPOINTS ---
@api_bp.route('/ai/summarize', methods=['POST'])
def ai_summarize():
    data = request.get_json() or {}
    text = data.get('text', '').strip()
    if not text:
        return jsonify({'status': 'error', 'message': 'Text parameter is required'}), 400
    
    if len(text) > 20000:
        return jsonify({'status': 'error', 'message': 'Text exceeds max allowed length of 20,000 characters'}), 400

    summary = ai_service.summarize(text)
    return jsonify({'status': 'success', 'result': summary})

@api_bp.route('/ai/rewrite', methods=['POST'])
def ai_rewrite():
    data = request.get_json() or {}
    text = data.get('text', '').strip()
    style = data.get('style', 'clear').strip()
    if not text:
        return jsonify({'status': 'error', 'message': 'Text parameter is required'}), 400
        
    rewritten = ai_service.rewrite(text, style)
    return jsonify({'status': 'success', 'result': rewritten})

@api_bp.route('/ai/explain', methods=['POST'])
def ai_explain():
    data = request.get_json() or {}
    text = data.get('text', '').strip()
    level = data.get('level', 'simple').strip()
    if not text:
        return jsonify({'status': 'error', 'message': 'Text parameter is required'}), 400
        
    explanation = ai_service.explain(text, level)
    return jsonify({'status': 'success', 'result': explanation})

@api_bp.route('/ai/questions', methods=['POST'])
def ai_questions():
    data = request.get_json() or {}
    text = data.get('text', '').strip()
    count = int(data.get('count', 5))
    if not text:
        return jsonify({'status': 'error', 'message': 'Text parameter is required'}), 400
        
    questions = ai_service.generate_questions(text, count)
    return jsonify({'status': 'success', 'result': questions})

# --- FAVORITES ENDPOINTS ---
@api_bp.route('/favorites', methods=['GET'])
def get_favorites():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'status': 'success', 'favorites': []})
        
    favs = Favorite.query.filter_by(user_id=user_id).all()
    return jsonify({'status': 'success', 'favorites': [f.tool_id for f in favs]})

@api_bp.route('/favorites', methods=['POST'])
def toggle_favorite():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'status': 'error', 'message': 'Authentication required for persistent DB favorites'}), 401
        
    data = request.get_json() or {}
    tool_id = data.get('tool_id')
    if not tool_id or not get_tool_by_id(tool_id):
        return jsonify({'status': 'error', 'message': 'Invalid tool_id'}), 400

    existing = Favorite.query.filter_by(user_id=user_id, tool_id=tool_id).first()
    if existing:
        db.session.delete(existing)
        db.session.commit()
        return jsonify({'status': 'success', 'action': 'removed', 'tool_id': tool_id})
    else:
        fav = Favorite(user_id=user_id, tool_id=tool_id)
        db.session.add(fav)
        db.session.commit()
        return jsonify({'status': 'success', 'action': 'added', 'tool_id': tool_id})

# --- FEEDBACK ENDPOINT ---
@api_bp.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json() or {}
    fb_type = data.get('feedback_type', 'suggestion')
    title = data.get('title', '').strip()
    description = data.get('description', '').strip()
    email = data.get('email', '').strip() or None

    if not title or not description:
        return jsonify({'status': 'error', 'message': 'Title and description are required'}), 400

    fb = Feedback(
        feedback_type=fb_type,
        title=title,
        description=description,
        email=email
    )
    db.session.add(fb)
    db.session.commit()

    return jsonify({'status': 'success', 'message': 'Thank you for your submission!'})
