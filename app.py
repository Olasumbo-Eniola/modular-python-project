from students import students
from utils.helpers import (
    get_average_score,
    get_highest_scoring_student,
    get_lowest_scoring_student,
    get_median_score,
)


LINE_WIDTH = 38


def display_students() -> None:
    print("=" * LINE_WIDTH)
    print("STUDENT SCORE REPORT".center(LINE_WIDTH))
    print("=" * LINE_WIDTH)

    if not students:
        print("No students found.".center(LINE_WIDTH))
        print("=" * LINE_WIDTH)
        return

    print(f"{'No.':<5}{'Student':<23}{'Score':>10}")
    print("-" * LINE_WIDTH)

    for number, student in enumerate(students, start=1):
        print(f"{number:<5}{student.name:<23}{student.score:>10}")

    print("-" * LINE_WIDTH)


def display_score_summary() -> None:
    highest = get_highest_scoring_student(students)
    lowest = get_lowest_scoring_student(students)
    average = get_average_score(students)
    median = get_median_score(students)

    print("SCORE SUMMARY".center(LINE_WIDTH))
    print("-" * LINE_WIDTH)

    if None in (highest, lowest, average, median):
        print("No scores are available.".center(LINE_WIDTH))
        print("=" * LINE_WIDTH)
        return

    print(f"{'Number of students:':<24}{len(students):>14}")
    print(f"{'Highest score:':<24}{highest.score:>6} ({highest.name})")
    print(f"{'Lowest score:':<24}{lowest.score:>6} ({lowest.name})")
    print(f"{'Average score:':<24}{average:>14.2f}")
    print(f"{'Median score:':<24}{median:>14.2f}")
    print("=" * LINE_WIDTH)


def main() -> None:
    display_students()
    display_score_summary()


if __name__ == "__main__":
    main()
