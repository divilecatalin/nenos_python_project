from pydantic import BaseModel

class UserDto(BaseModel):
    username : str
    email : str
    role : str
    endorsements : int = 0
    reports : int = 0
    banned : bool = False