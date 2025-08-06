from pydantic import BaseModel 

class MatchingRequest(BaseModel):
    document_A: str
    document_B: str 

