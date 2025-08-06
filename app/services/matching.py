from app.utils import matching_information
from fastapi import HTTPException, status
from app.schemas import MatchingRequest

async def matching_info(request: MatchingRequest):
    try:
        return await matching_information(request.document_A, request.document_B)
    except Exception as ex:
        raise HTTPException(
            detail = str(ex),
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR
        )