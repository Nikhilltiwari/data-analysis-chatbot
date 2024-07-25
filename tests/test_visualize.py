from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_visualize_query():
    response = client.post("/api/v1/visualize", json={"query": "sales trend in Q1", "filename": "filename.csv"})
    assert response.status_code == 200
    assert "plot_url" in response.json()
