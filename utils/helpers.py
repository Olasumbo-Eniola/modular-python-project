from models import Student


def get_highest_scoring_student(students: list[Student]) -> Student | None:
    if not students:
        return None

    return max(students, key=lambda student: student.score)


def get_lowest_scoring_student(students: list[Student]) -> Student | None:
    if not students:
        return None

    return min(students, key=lambda student: student.score)
