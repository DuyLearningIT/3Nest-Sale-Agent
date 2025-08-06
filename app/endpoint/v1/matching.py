from app.services import matching
from fastapi import APIRouter, status

matching_router = APIRouter(
    prefix="/matching",
    tags=["Matching Services"]
)

@matching_router.post('/')
async def matching_info(document_A: str, document_B: str):
    data = await matching.matching_info(document_A, document_B)
    return {
        'mess' : 'Match information successfully !',
        'status_code': status.HTTP_200_OK,
        'data' : data
    }