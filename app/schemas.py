from pydantic import BaseModel, EmailStr, validator, Field
from datetime import date

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    role: str  # viewer / analyst / admin


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    is_active: bool

    class Config:
        from_attributes = True


class RecordCreate(BaseModel):
    amount: float = Field(gt=0)
    type: str
    category: str
    date: date
    notes: str

    @validator("type")
    def validate_type(cls, value):
        if value not in ["income", "expense"]:
            raise ValueError("Type must be 'income' or 'expense'")
        return value


class RecordResponse(BaseModel):
    id: int
    amount: float
    type: str
    category: str
    date: date
    notes: str
    user_id: int

    class Config:
        from_attributes = True        