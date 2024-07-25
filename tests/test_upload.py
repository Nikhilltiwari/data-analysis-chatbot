from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_upload_file():
    response = client.post("/api/v1/upload", files={"file": ("filename.csv", "date,sales\n2023-01-01,100\n2023-01-02,150")})
    assert response.status_code == 200
    assert response.json() == {"message": "File uploaded successfully", "columns": ["date", "sales"]}
