import os
import pytest
from app import app
@pytest.fixture
def client():
app.config['TESTING'] = True
with app.test_client() as client:
yield client
def test_hello(client):
response = client.get('/')
assert response.data.decode() == "Hello, World!"
assert response.status_code == 200
def test_env(client, monkeypatch):
monkeypatch.setenv("MY_ENV_VAR", "TestValue")
response = client.get('/env')
assert "Environment Variable: TestValue" in response.data.decode()
assert response.status_code == 200