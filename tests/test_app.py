import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Products" in response.data

def test_add_to_cart(client):
    response = client.get('/add/1', follow_redirects=True)
    assert response.status_code == 200
    assert b"Red Dress" in response.data
