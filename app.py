from students import students
from utils.helpers import get_highest_scoring_student, get_lowest_scoring_student


def display_students():
    print("Student Scores")
    print("-" * 30)

    for student in students:
        print("{}: {}".format(student["name"], student["score"]))


def display_score_summary():
    highest = get_highest_scoring_student(students)
    lowest = get_lowest_scoring_student(students)

    print("\nScore Summary")
    print("-" * 30)
    print("Highest: {} ({})".format(highest["name"], highest["score"]))
    print("Lowest: {} ({})".format(lowest["name"], lowest["score"]))


def main():
    display_students()
    display_score_summary()


if __name__ == "__main__":
    main()
