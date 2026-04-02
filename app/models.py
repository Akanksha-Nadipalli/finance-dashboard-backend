from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    role = Column(String)  # viewer / analyst / admin
    is_active = Column(Boolean, default=True)


class FinancialRecord(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    type = Column(String)  # income / expense
    category = Column(String)
    date = Column(Date)
    notes = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))