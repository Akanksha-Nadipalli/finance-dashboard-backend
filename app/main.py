from fastapi import FastAPI, Depends, HTTPException
from app.database import engine, Base, get_db
from app import models, schemas
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional


app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)


def get_current_user(db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == 1).first()

    if not user.is_active:
        raise HTTPException(status_code=403, detail="Inactive user")
    return user    

def check_role(user, allowed_roles):
    if user.role not in allowed_roles:
        raise HTTPException(status_code=403, detail="Access denied")

@app.get("/")
def root():
    return {"message": "Backend running 🚀"}


@app.get("/users", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@app.get("/records", response_model=list[schemas.RecordResponse])
def get_records(
    type: Optional[str] = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    check_role(user, ["analyst", "admin"])

    query = db.query(models.FinancialRecord)

    if type:
        query = query.filter(models.FinancialRecord.type == type)

    return query.offset(skip).limit(limit).all()

@app.get("/dashboard/category")
def category_breakdown(db: Session = Depends(get_db)):
    results = db.query(
        models.FinancialRecord.category,
        func.sum(models.FinancialRecord.amount)
    ).group_by(models.FinancialRecord.category).all()

    return [{"category": r[0], "total": r[1]} for r in results]


@app.get("/dashboard/recent")
def recent_transactions(db: Session = Depends(get_db)):
    records = db.query(models.FinancialRecord)\
        .order_by(models.FinancialRecord.id.desc())\
        .limit(5).all()

    return records

@app.get("/dashboard/trends")
def monthly_trends(db: Session = Depends(get_db)):
    results = db.query(
        models.FinancialRecord.date,
        func.sum(models.FinancialRecord.amount)
    ).group_by(models.FinancialRecord.date).all()

    return [{"date": r[0], "total": r[1]} for r in results]


@app.get("/dashboard")
def get_dashboard(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):

    total_income = db.query(func.sum(models.FinancialRecord.amount))\
        .filter(models.FinancialRecord.type == "income")\
        .scalar() or 0

    total_expense = db.query(func.sum(models.FinancialRecord.amount))\
        .filter(models.FinancialRecord.type == "expense")\
        .scalar() or 0

    net_balance = total_income - total_expense

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": net_balance
    }

@app.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):

    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.name = user.name
    db_user.email = user.email
    db_user.role = user.role

    db.commit()
    db.refresh(db_user)

    return db_user

@app.put("/records/{record_id}", response_model=schemas.RecordResponse)
def update_record(
    record_id: int,
    record: schemas.RecordCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    check_role(user, ["admin"])

    db_record = db.query(models.FinancialRecord).filter(models.FinancialRecord.id == record_id).first()

    if not db_record:
        raise HTTPException(status_code=404, detail="Record not found")

    db_record.amount = record.amount
    db_record.type = record.type
    db_record.category = record.category
    db_record.date = record.date
    db_record.notes = record.notes

    db.commit()
    db.refresh(db_record)

    return db_record

@app.delete("/records/{record_id}")
def delete_record(
    record_id: int,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    check_role(user, ["admin"])

    db_record = db.query(models.FinancialRecord).filter(models.FinancialRecord.id == record_id).first()

    if not db_record:
        raise HTTPException(status_code=404, detail="Record not found")

    db.delete(db_record)
    db.commit()

    return {"message": "Record deleted successfully"}


@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(models.User).filter(models.User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = models.User(
        name=user.name,
        email=user.email,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@app.post("/records", response_model=schemas.RecordResponse)
def create_record(
    record: schemas.RecordCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    check_role(user, ["admin"])

    new_record = models.FinancialRecord(
        amount=record.amount,
        type=record.type,
        category=record.category,
        date=record.date,
        notes=record.notes,
        user_id=1
    )

    db.add(new_record)
    db.commit()
    db.refresh(new_record)

    return new_record

