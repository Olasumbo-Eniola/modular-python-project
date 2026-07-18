def get_highest_scoring_student(students):
    if not students:
        raise ValueError("The student list cannot be empty.")

    return max(students, key=lambda student: student["score"])


def get_lowest_scoring_student(students):
    if not students:
        raise ValueError("The student list cannot be empty.")

    return min(students, key=lambda student: student["score"])
