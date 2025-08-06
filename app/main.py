from fastapi import FastAPI, status
from app.endpoint.v1 import matching_router


app = FastAPI()

app.include_router(matching_router)

@app.get('/')
async def default():
    return {
        'mess' : 'API is running!',
        'status_code' : status.HTTP_200_OK
    }