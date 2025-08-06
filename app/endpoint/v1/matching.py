from app.services import matching
from fastapi import APIRouter, status
from app.schemas import MatchingRequest

matching_router = APIRouter(
    prefix="/matching",
    tags=["Matching Services"]
)

@matching_router.post('/match-information')
async def matching_info(request: MatchingRequest):
    data = await matching.matching_info(request)
    return {
        'mess' : 'Match information successfully !',
        'status_code': status.HTTP_200_OK,
        'data' : data
    }