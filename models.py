"""Define the validated data model used for student records."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Student:
    """Represent one student and ensure their data is valid."""

    name: str
    score: int

    def __post_init__(self):
        """Validate and normalize the student's name and score."""
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("Student name must be a non-empty string.")

        if type(self.score) is not int:
            raise TypeError("Student score must be an integer.")

        if not 0 <= self.score <= 100:
            raise ValueError("Student score must be between 0 and 100.")

        object.__setattr__(self, "name", self.name.strip())
