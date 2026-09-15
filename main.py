from fastapi import FastAPI

# ============================================================
# FASTAPI WORKSHOP
# Patient Management System API
# ============================================================

app = FastAPI(
    title="Patient Management System API",
    description="Workshop Starter Code for Learning FastAPI",
    version="1.0.0"
)

# ============================================================
# HOME ENDPOINT
# ============================================================

@app.get("/")
def home():
    """
    Welcome Endpoint
    """
    return {
        "message": "Welcome to the Patient Management System API!"
    }


# ============================================================
# ABOUT ENDPOINT
# ============================================================

@app.get("/about")
def about():
    """
    About this API
    """
    return {
        "message": "A REST API built using FastAPI to manage patient records."
    }


# ============================================================
# PART 1 : READING JSON DATA
# ============================================================

# TODO:
# 1. Import the json module.
# 2. Create a function called load_data().
# 3. Read the patients.json file.
# 4. Return the data.

import json 

def load_data():
    with open("patients.json", "r") as file:
        return json.load(file)
    



# ============================================================
# PART 2 : VIEW ALL PATIENTS
# ============================================================

# TODO:
# Create an endpoint:
#
# GET /view
#
# Return all patients.
@app.get("/view")
def get_all_patients():
    data=load_data()
    return data



# ============================================================
# PART 3 : PATH PARAMETERS
# ============================================================

# TODO:
# Create:
#
# GET /patient/{patient_id}
#
# Learn:
# - Path Parameters
# - Path()
@app.get("/patient/{patient_id}")
def get_patient(patient_id: int):
    data=load_data()
    return data[patient_id]


# ============================================================
# PART 4 : HTTP EXCEPTIONS
# ============================================================

# TODO:
#
# Raise HTTPException
#
# Status Code:
# 404
from fastapi import HTTPException
@app.get("/patient/{patient_id}")
def get_patient(patient_id: int):
    data = load_data()
    
    # Check if the patient_id is valid (assuming 'data' is a list)
    if patient_id < 0 or patient_id >= len(data):
        raise HTTPException(status_code=404, detail="Patient not found")
        
    return data[patient_id]



# ============================================================
# PART 5 : QUERY PARAMETERS
# ============================================================

# TODO:
#
# GET /sort
#
# Learn:
# - Query()
# - Sorting
@app.get("/sort")
def sort_patients(sort_by: str = "name"):
    data = load_data()
    return sorted(data, key=lambda x: x[sort_by])


# ============================================================
# PART 6 : PYDANTIC MODELS
# ============================================================

# TODO:
#
# Create:
#
# class Patient(BaseModel):
#     ...
from pydantic import BaseModel, Field

class Patient(BaseModel):
    id: str = Field(..., description="Unique patient ID", examples=["P001"])
    name: str = Field(..., description="Full name of the patient")
    city: str = Field(..., description="City where the patient lives")
    age: int = Field(..., gt=0, description="Age of the patient")
    gender: str = Field(..., description="Gender of the patient")
    height: float = Field(..., gt=0, description="Height in meters")
    weight: float = Field(..., gt=0, description="Weight in kilograms")


# ============================================================
# PART 7 : CREATE PATIENT
# ============================================================

# TODO:
#
# POST /create
@app.post("/create")
def create_patient(patient: Patient):
    data=load_data()

    data[patient.id]=patient.model_dump()
    with open("patients.json", "w") as file:
        json.dump(data, file, indent=4)
    return {"message": "Patient created successfully", "patient": patient}
        


# ============================================================
# PART 8 : UPDATE PATIENT
# ============================================================

# TODO:
#
# PUT /edit/{patient_id}
@app.put("/edit/{patient_id}")
def update_patient(patient_id: str, patient: Patient):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
        
    data[patient_id] = patient.model_dump(exclude={"id"})
    
    with open("patients.json", "w") as file:
        json.dump(data, file, indent=4)
    return {"message": "Patient updated successfully", "patient": patient}


# ============================================================
# PART 9 : DELETE PATIENT
# ============================================================

# TODO:
#
# DELETE /delete/{patient_id}
@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
        
    del data[patient_id]
    
    with open("patients.json", "w") as file:
        json.dump(data, file, indent=4)
    return {"message": "Patient deleted successfully", "id": patient_id}
