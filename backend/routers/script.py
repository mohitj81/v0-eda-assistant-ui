from fastapi import APIRouter
from services.script_service import generate_cleaning_script

router = APIRouter(prefix="/script", tags=["Script Generator"])

@router.get("/{dataset_id}")
async def get_script(dataset_id: str):
    script = generate_cleaning_script(dataset_id)
    return {"script": script}
