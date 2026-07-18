def get_highest_scoring_student(students):
    if not students:
        return None

    return max(students, key=lambda student: student["score"])


def get_lowest_scoring_student(students):
    if not students:
        return None

    return min(students, key=lambda student: student["score"])
