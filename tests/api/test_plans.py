from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_upload_valid_md_file(tmp_path):
    file_path = tmp_path / "test.md"
    file_path.write_text("# My Markdown Plan")

    with file_path.open("rb") as f:
        response = client.post(
            "/api/plans", files={"file": ("test.md", f, "text/markdown")}
        )

    assert response.status_code == 200
    data = response.json()
    assert "plan_id" in data
    assert data["filename"] == "test.md"


def test_upload_invalid_file_extension(tmp_path):
    file_path = tmp_path / "invalid.txt"
    file_path.write_text("Not a markdown file")

    with file_path.open("rb") as f:
        response = client.post(
            "/api/plans", files={"file": ("invalid.txt", f, "text/plain")}
        )

    assert response.status_code == 400
    assert response.json()["detail"] == "Only .md files are allowed"
