from pydantic import BaseModel, conint, constr, confloat, conlist, field_validator
from typing import Optional
import re

class StudentBase(BaseModel):
    # id: int
    first_name : str
    last_name : str
    email: str

    @field_validator('first_name')
    @classmethod
    def validate_last_name(cls, value):
        if len(value) < 2:
            raise ValueError('Name Must be More than 2 letters')
        if re.match(r'\W',value):
            raise ValueError('Name Must not include a special character')
        if re.match(r'\d',value):
            raise ValueError('Name Must not include a Number')
        return value.title()


class StudentUpdateSchema(BaseModel):
    first_name : Optional[str] = None 
    last_name :  Optional[str] = None 
    email:  Optional[str] = None 