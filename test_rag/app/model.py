from pydantic import BaseModel


class VirtualAssistant(BaseModel):
    availability: str
    next_open_time_slot: str 
    