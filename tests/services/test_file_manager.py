from io import BytesIO

import pytest
from fastapi import UploadFile

from app.services.file_manager import save_plan_file


@pytest.mark.asyncio
async def test_save_plan_file_creates_file(tmp_path):
    plan_id = "test-plan-id"
    content = b"# Sample Plan Content"

    file = UploadFile(filename="test.md", file=BytesIO(content))
    upload_dir = tmp_path
    output_path = upload_dir / f"{plan_id}.md"

    # Monkeypatch UPLOAD_DIR to use temp
    from app.services import file_manager

    file_manager.UPLOAD_DIR = upload_dir

    await save_plan_file(file, plan_id)

    assert output_path.exists()
    assert output_path.read_bytes() == content
