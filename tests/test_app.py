import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
def test_home():
    app.testing = True
    client = app.test_client()

    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'
