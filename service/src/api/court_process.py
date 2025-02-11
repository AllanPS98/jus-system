from datetime import datetime
from src.controllers.court_process import CourtProcessController
from fastapi import APIRouter, HTTPException
from typing import List, Optional
from src.model.court_process import CourtProcess
from pydantic import BaseModel

router = APIRouter()

class PostCourtProcessPayload(BaseModel):
    process_number: str

class PostCourtProcessResult(BaseModel):
    id_process: str

class CourtProcess(BaseModel):
    court_process_id: str
    control_process_id: str
    court_name: Optional[str]
    process_number: Optional[str]
    degree: Optional[int]
    process_class: Optional[str]
    area: Optional[str]
    subject: Optional[str]
    distribution_date: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class GetCourtProcessResult(BaseModel):
    page: int
    amount: int
    total: int
    last_page: int
    data: List[CourtProcess]
    
    class Config:
        arbitrary_types_allowed = True
    

@router.post("/court-process/", response_model=PostCourtProcessResult)
def create_court_process(payload: PostCourtProcessPayload):
    controller = CourtProcessController()
    result = controller.crawl_process(payload.process_number)
    return_post_court_process = PostCourtProcessResult(id_process=str(result))
    return return_post_court_process

@router.get("/court-process/", response_model=GetCourtProcessResult)
def get_court_processes(value: str, page: int = 1, amount: int = 10, search_by: str = 'process_number'):
    controller = CourtProcessController()
    result = controller.get_process(page, amount, search_by, value)
    list_data = []
    for item in result['data']:
        court_process = CourtProcess(
            court_process_id=item['court_process_id'],
            control_process_id=item['control_process_id'],
            court_name=item['court_name'],
            process_number=item['process_number'],
            degree=item['degree'],
            process_class=item['process_class'],
            area=item['area'],
            subject=item['subject'],
            distribution_date=item['distribution_date'],
            created_at=item['created_at'],
            updated_at=item['updated_at']
        )
        list_data.append(court_process)
    return_get_court_process = GetCourtProcessResult(
        page=page,
        amount=amount,
        total=result['total'],
        last_page=result['last_page'],
        data=list_data
    )
    
    return return_get_court_process