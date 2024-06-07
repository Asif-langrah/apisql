from fastapi import FastAPI
from sqlmodel import Field, SQLModel,create_engine,Session,select

DATABASE_KEY = 'postgresql://neondb_owner:LAYBh2ETrNs0@ep-shrill-shadow-a1dtu58s.ap-southeast-1.aws.neon.tech/friday-db?sslmode=require'

class User(SQLModel,table=True):
    name: str = Field(default=str, primary_key=True)
    fatherName: str = Field(default=str, primary_key=True)
    mobileNo:int = Field(default=int, primary_key=True)

engine = create_engine(DATABASE_KEY, echo=True)
SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.get("/user")
def get_user():
    with Session(engine) as session:
        user = session.exec(select(User)).all()
    return user

@app.post("/user")
def add_user(name:str,fatherName:str,mobileNo:int):
    with Session(engine) as session:
        session.add(User(name=name,fatherName=fatherName,mobileNo=mobileNo))
        session.commit()
    return "task added successfully"


