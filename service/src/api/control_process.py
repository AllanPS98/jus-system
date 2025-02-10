from datetime import datetime
from src.controllers.control_process import ControlProcessController
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class ControlProcess(BaseModel):
    control_process_id: str
    status: str
    message: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

@router.get("/control-process/{control_process_id}", response_model=ControlProcess)
def get_control_process(control_process_id: str):
    controller = ControlProcessController()
    result = controller.get_control_process(control_process_id)
    control_process = ControlProcess(
        control_process_id=result['control_process_id'],
        status=result['status'],
        message=result['message'],
        created_at=result['created_at'],
        updated_at=result['updated_at']
    )
    return control_process