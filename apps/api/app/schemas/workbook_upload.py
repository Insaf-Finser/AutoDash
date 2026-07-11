from pydantic import BaseModel


class UploadResponse(BaseModel):
    id:str

    name:str

    status:str