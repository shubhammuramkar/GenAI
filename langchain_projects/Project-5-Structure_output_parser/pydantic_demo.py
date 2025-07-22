from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Review(BaseModel):
    name: str = "shubham" # default value
    age : Optional[int] = None
    email:  EmailStr #Optional[EmailStr] = None 
    cgpa: float = Field(gt=0, le=10, default=5 ,description="CGPA must be between 0 and 10")

new_student = {"age": "25", "email": "abc@ac.com", "cgpa": 9}

student = Review(**new_student)

student_dict = dict(student)

print(student_dict['name'])

student_json = student.model_dump_json()

print(student_json)