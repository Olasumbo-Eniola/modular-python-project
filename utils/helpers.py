"""Provide reusable calculations for collections of students."""

from statistics import mean, median

from models import Student


def get_highest_scoring_student(students: list[Student]) -> Student | None:
    """Return the highest-scoring student, or None for an empty list."""
    if not students:
        return None

    return max(students, key=lambda student: student.score)


def get_lowest_scoring_student(students: list[Student]) -> Student | None:
    """Return the lowest-scoring student, or None for an empty list."""
    if not students:
        return None

    return min(students, key=lambda student: student.score)


def get_average_score(students: list[Student]) -> float | None:
    """Return the mean score, or None when no students are provided."""
    if not students:
        return None

    return mean(student.score for student in students)


def get_median_score(students: list[Student]) -> float | None:
    """Return the median score, or None when no students are provided."""
    if not students:
        return None

    return median(student.score for student in students)
