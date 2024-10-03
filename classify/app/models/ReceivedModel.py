from pydantic import BaseModel

class Received(BaseModel):
    id: str
    cat_dac: int
    cat_cla: int