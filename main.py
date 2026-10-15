from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4,UUID
app = FastAPI(title="First API")

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

data = []

@app.get("/")
def home():
    return {"message":"Welcome to our api!"}



@app.get("/getEmployee")
def get_employees():
    return data


@app.post("/employees")
def add_employee(name:str,position:str):
    id = uuid4()
    employee = {"id":id,"name":name,"position":position}

    data.append(employee)

    return employee

@app.put("/employees")
def update_employee(id:UUID,name:str,position:str):
    for employee in data:
        if employee["id"] == id:
            employee["name"] = name
            employee["position"] = position

            return employee
    return {"message":"Employee Not found!"}


@app.delete("/employees")
def delete_employee(id:UUID):
    for i in range(len(data)):
        if data[i]["id"] == id:
            employee = data.pop(i)

            return employee
    return {"message":"Employee Not found!"}


