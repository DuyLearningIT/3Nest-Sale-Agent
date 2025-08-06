from app.utils import matching_information
from fastapi import HTTPException, status

async def matching_info(document_A, document_B):
    try:
        return await matching_information(document_A, document_B)
    except Exception as ex:
        raise HTTPException(
            detail = str(ex),
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR
        )