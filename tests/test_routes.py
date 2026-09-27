import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"ToolHub" in rv.data
    assert b"Free Tools. Open Source." in rv.data

def test_all_tools_page(client):
    rv = client.get('/tools')
    assert rv.status_code == 200
    assert b"All Online Tools" in rv.data

def test_category_page(client):
    rv = client.get('/category/developer')
    assert rv.status_code == 200
    assert b"Developer Tools" in rv.data

def test_tool_detail_page(client):
    rv = client.get('/tools/json-formatter')
    assert rv.status_code == 200
    assert b"JSON Formatter" in rv.data

def test_nonexistent_tool(client):
    rv = client.get('/tools/non-existent-tool-slug')
    assert rv.status_code == 404
