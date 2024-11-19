from pydantic import BaseModel

class APIStatusDto(BaseModel):
    running: bool
    db_name: str