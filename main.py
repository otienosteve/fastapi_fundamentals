# @app.post('/')
# @app.patch('/')
# @app.delete('/')
# @app.put('/')
from fastapi import FastAPI
from models import Student, session
from schemas import StudentBase, StudentUpdateSchema
app  = FastAPI()
from typing import List

@app.get('/home')
def home():
    return {"msg": "welcome to fastapi "}


# serialised data

@app.get('/students')
def students() -> List[StudentBase]:
    students = session.query(Student).all()
    return students


@app.get('/students/{id}')
def student(id: int) -> StudentBase:
    student = session.query(Student).filter_by(id=id).first()
    return student

@app.post('/students')
def add_student(payload: StudentBase) -> StudentBase:
    user_data = payload.model_dump()
    new_student = Student(**user_data)
    session.add(new_student)
    session.commit()
    return new_student


@app.patch('/students/{id}')
def update_student(id: int, payload:StudentUpdateSchema) -> StudentBase:
    student = session.query(Student).filter_by(id=id).first()
    print(student)
    for key, value in payload.model_dump(exclude_unset=True).items():
        if value is None:
            continue
        setattr(student, key,value)
    session.add(student)  
    session.commit()  
    return student 

@app.delete('/students/{id}')
def delete_student(id):
    student = session.query(Student).filter_by(id=id).first()
    session.delete(student)
    session.commit()
    return {'msg': f" Student with {id=} has been deleted successfully"}







