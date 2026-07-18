from students import students
from utils.helpers import get_highest_scoring_student, get_lowest_scoring_student


def display_students():
    print("Student Scores")
    print("-" * 30)

    if not students:
        print("No students found.")
        return

    for student in students:
        print("{}: {}".format(student["name"], student["score"]))


def display_score_summary():
    highest = get_highest_scoring_student(students)
    lowest = get_lowest_scoring_student(students)

    print("\nScore Summary")
    print("-" * 30)

    if highest is None or lowest is None:
        print("No scores are available.")
        return

    print("Highest: {} ({})".format(highest["name"], highest["score"]))
    print("Lowest: {} ({})".format(lowest["name"], lowest["score"]))


def main():
    display_students()
    display_score_summary()


if __name__ == "__main__":
    main()
