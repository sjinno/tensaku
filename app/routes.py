from fastapi import APIRouter
from app.models import MessageRequest, MessageResponse
from app.services import correct_message

router = APIRouter()


@router.post("/correct", response_model=MessageResponse)
async def correct(request: MessageRequest):
    return await correct_message(request.message)
