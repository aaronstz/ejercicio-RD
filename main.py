from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from ejercicio_RD import models, database


app = FastAPI()
security = HTTPBasic()

# Crear la base de datos
models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# autenticación
def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"
    correct_password = "password"
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/input/{my_target_field}")
def input_data(my_target_field: str, data: dict, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(authenticate)):
    if my_target_field not in ["field_1", "author", "description"]:
        raise HTTPException(status_code=400, detail=f"{my_target_field} no es un campo válido para convertir a mayúscula")

    data[my_target_field] = data[my_target_field].upper()
    db_data = models.DataModel(**data)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return {"id": db_data.id}

@app.get("/data/{id}")
def get_data(id: int, db: Session = Depends(get_db)):
    db_data = db.query(models.DataModel).filter(models.DataModel.id == id).first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_data