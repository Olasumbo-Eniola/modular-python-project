
"""Create and provide student records for the application."""

from collections.abc import Iterable

from models import Student


type StudentRecord = tuple[str, int]

# A tuple protects the original sample records from accidental modification.
DEFAULT_STUDENT_RECORDS: tuple[StudentRecord, ...] = (
    ("Ada", 84),
    ("Chidi", 92),
    ("Fatima", 76),
    ("Tunde", 88),
)


def create_students(records: Iterable[StudentRecord]) -> list[Student]:
    """Convert name-and-score records into validated Student objects."""
    return [Student(name=name, score=score) for name, score in records]


def get_default_students() -> list[Student]:
    """Return a new list containing the application's sample students."""
    return create_students(DEFAULT_STUDENT_RECORDS)
