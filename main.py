from fastapi import FastAPI, Depends, HTTPException
from database import engine, SessionLocal
from sqlalchemy.orm import Session

import models, crud, schemas

models.Base.metadata.create_all(bind=engine)

def get_db():
    db= SessionLocal()
    try:
        yield db

    finally:
        db.close() #zawsze zamykamy połączenie do bazy  


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/users/", response_model = schemas.User) #co się dzieje po przekazaniu recquesta
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)): #user przekazuje takie dane, które można zmapować na UserCreate
    db_user = crud.get_user_by_email(db, email = user.email)
    if db_user:
        raise HTTPException(status_code = 400, detail="Email already registered")

    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model = schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user[0]