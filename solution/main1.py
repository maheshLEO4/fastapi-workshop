from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json


app = FastAPI()

class Patient(BaseModel):
    
    id: Annotated[str, Field(..., description= 'ID of the patient', example=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City where the patient lives')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['Male', 'Female', 'Other'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in m')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient in kg')]
    
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal weight'
        elif self.bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'
        

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
        
    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)

@app.get("/")
def hello():
    return {"message" : "Patient Management System API"}

@app.get("/about")
def about():
    return{"message" : "A fully functional API to manage your patient records."}

@app.get('/view')
def view():
    data = load_data()
    
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):
    
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]

    raise HTTPException(status_code=404, detail='patient not found!')
    
@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in ascending or descending order')):
    
    valid_feilds = ['height', 'weight', 'bmi']
    
    if sort_by not in valid_feilds:
        raise HTTPException(status_code=400, detail=f'Invalid feild select from {valid_feilds}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()
    
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse= sort_order)
    
    return sorted_data

@app.post('/create')
def create_patient(patient: Patient):
    
    # load existing data
    data = load_data()
    
    # check if the patient id already exisits
    if patient .id in data:
        raise HTTPException(status_code = 400, detail= 'Patient Already Exsists')
        
    # new patient add to the database
    data[patient.id] = patient.model_dump(exclude=['id'])
    
    # save into the json file
    save_data(data)
    
    return JSONResponse(status_code = 201, content={'message': 'Patient created successfully!'})


class PatientUpdate(BaseModel):
    
    name: Annotated[Optional[str], Field(description='Name of the patient')]
    city: Annotated[Optional[str], Field(description='City where the patient lives')]
    age: Annotated[Optional[int], Field(gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Optional[Literal['Male', 'Female', 'Other']], Field(description='Gender of the patient')]
    height: Annotated[Optional[float], Field(gt=0, description='Height of the patient in m')]
    weight: Annotated[Optional[float], Field(gt=0, description='Weight of the patient in kg')]
    
@app.put('/edit/{patient_id}')

def update_patient(patient_id: str, patient_update: PatientUpdate):
    
    data = load_data()
    
    if patient_id not in data:
        raise HTTPException(status_code= 404, detail='Patient not found!')
    
    existing_patient_info = data[patient_id]
    
    updated_patient_info = patient_update.model_dump(exclude_unset=True)
    
    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value
        
        patient_pydantic_object = Patient(id=patient_id, **existing_patient_info)
        existing_patient_info = patient_pydantic_object.model_dump(exclude=['id'])
        
        data[patient_id] = existing_patient_info
    save_data(data)
    
    return JSONResponse(status_code=200, content={'message': 'Patient updated successfully!'})


@app.delete('/delete/{patient_id}')

def delete_patient(patient_id: str):
    
    data = load_data()
    
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]
    
    save_data(data)
    
    return JSONResponse(status_code= 200, content={'message': 'Pateient deleted.'})