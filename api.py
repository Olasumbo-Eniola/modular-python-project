"""Expose student records and score statistics through FastAPI."""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

from models import Student
from students import get_default_students
from utils.helpers import (
    get_average_score,
    get_highest_scoring_student,
    get_lowest_scoring_student,
    get_median_score,
)


class StudentInput(BaseModel):
    """Validate data received when a student is created."""

    name: str = Field(min_length=1)
    score: int = Field(ge=0, le=100)


app = FastAPI(title="Student Score API", version="1.0.0")
students = get_default_students()


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    """Confirm that the service is available."""
    return {"status": "ok"}


@app.get("/students", tags=["students"])
def list_students() -> list[Student]:
    """Return every student record."""
    return students


@app.get("/students/summary", tags=["students"])
def score_summary() -> dict[str, object]:
    """Return summary statistics for all students."""
    highest = get_highest_scoring_student(students)
    lowest = get_lowest_scoring_student(students)
    return {
        "count": len(students),
        "highest": highest,
        "lowest": lowest,
        "average": get_average_score(students),
        "median": get_median_score(students),
    }


@app.post("/students", status_code=status.HTTP_201_CREATED, tags=["students"])
def create_student(payload: StudentInput) -> Student:
    """Create and return a validated student record."""
    if any(student.name.casefold() == payload.name.strip().casefold() for student in students):
        raise HTTPException(status_code=409, detail="Student already exists.")
    student = Student(name=payload.name, score=payload.score)
    students.append(student)
    return student
