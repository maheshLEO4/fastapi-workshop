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


# ============================================================
# PART 2 : VIEW ALL PATIENTS
# ============================================================

# TODO:
# Create an endpoint:
#
# GET /view
#
# Return all patients.


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


# ============================================================
# PART 4 : HTTP EXCEPTIONS
# ============================================================

# TODO:
#
# Raise HTTPException
#
# Status Code:
# 404


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


# ============================================================
# PART 6 : PYDANTIC MODELS
# ============================================================

# TODO:
#
# Create:
#
# class Patient(BaseModel):
#     ...


# ============================================================
# PART 7 : CREATE PATIENT
# ============================================================

# TODO:
#
# POST /create


# ============================================================
# PART 8 : UPDATE PATIENT
# ============================================================

# TODO:
#
# PUT /edit/{patient_id}


# ============================================================
# PART 9 : DELETE PATIENT
# ============================================================

# TODO:
#
# DELETE /delete/{patient_id}