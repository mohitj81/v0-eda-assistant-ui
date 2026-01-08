import os
import uuid
from fastapi import UploadFile

UPLOAD_DIR = "backend/storage/uploaded/"

def save_uploaded_file(file: UploadFile):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # Create unique dataset ID
    dataset_id = str(uuid.uuid4())

    # File path
    file_path = os.path.join(UPLOAD_DIR, f"{dataset_id}.csv")

    # Save file
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return dataset_id, file_path
