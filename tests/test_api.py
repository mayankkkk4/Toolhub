import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_api_tools_list(client):
    rv = client.get('/api/tools')
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['status'] == 'success'
    assert len(data['tools']) > 0

def test_api_tools_search(client):
    rv = client.get('/api/tools?search=json')
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['status'] == 'success'
    assert any(t['id'] == 'json-formatter' for t in data['tools'])

def test_api_categories(client):
    rv = client.get('/api/categories')
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['status'] == 'success'
    assert len(data['categories']) == 8

def test_api_ai_summarize(client):
    rv = client.post('/api/ai/summarize', json={'text': 'ToolHub is an open source platform. It is free to use. Data is private.'})
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['status'] == 'success'
    assert 'result' in data
