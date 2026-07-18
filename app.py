from students import students
from utils.helpers import get_highest_scoring_student, get_lowest_scoring_student


def display_students() -> None:
    print("Student Scores")
    print("-" * 30)

    if not students:
        print("No students found.")
        return

    for student in students:
        print(f"{student.name}: {student.score}")


def display_score_summary() -> None:
    highest = get_highest_scoring_student(students)
    lowest = get_lowest_scoring_student(students)

    print("\nScore Summary")
    print("-" * 30)

    if highest is None or lowest is None:
        print("No scores are available.")
        return

    print(f"Highest: {highest.name} ({highest.score})")
    print(f"Lowest: {lowest.name} ({lowest.score})")


def main() -> None:
    display_students()
    display_score_summary()


if __name__ == "__main__":
    main()
