from pydantic import BaseModel, validator
from pydantic import ValidationError
from errors import HttpError

class CreateAdv(BaseModel):

    title: str
    description: str
    owner: str

    @validator('title')
    def validate_title(cls, value: str):
        if  len(value) < 3:
            raise ValueError('title mast be correct')
        return value


def validate_create_adv(json_data):
    try:
        adv_schema = CreateAdv(**json_data)
        return adv_schema.dict()
    except ValidationError as er:
        raise HttpError(status_code=400, message=er.errors())
