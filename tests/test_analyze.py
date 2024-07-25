from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_analyze_query():
    response = client.post("/api/v1/analyze", json={"query": "average sales in Q1", "filename": "filename.csv"})
    assert response.status_code == 200
    assert "result" in response.json()
