from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import re
import os

app = FastAPI()

# Define a request model
class DataInput(BaseModel):
    data: List[str]

# User details
USER_ID = os.getenv("USER_ID", "suraj_raj_15052004")
EMAIL = os.getenv("EMAIL", "22BCS15623@cuchd.in")
ROLL_NUMBER = os.getenv("ROLL_NUMBER", "22BCS15623")

@app.get("/bfhl")
async def get_operation_code():
    return {"operation_code": 1}

@app.post("/bfhl")
async def process_data(input_data: DataInput):
    numbers = []
    alphabets = []

    for item in input_data.data:
        if re.fullmatch(r'\d+', item):  # Check if it's a number
            numbers.append(item)
        elif re.fullmatch(r'[a-zA-Z]', item):  # Check if it's a single alphabet
            alphabets.append(item)
        else:
            raise HTTPException(status_code=400, detail=f"Invalid input: {item}")

    highest_alphabet = max(alphabets, key=lambda x: x.upper()) if alphabets else []

    return {
        "is_success": True,
        "user_id": USER_ID,
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": [highest_alphabet] if highest_alphabet else []
    }
