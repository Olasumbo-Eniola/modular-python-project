# SEN 401 Student Score Application

The application displays a list of students
and identifies the students with the highest and lowest scores.

## Project Structure

```text
sen_401/
├── app.py              # Starts the application and displays the results
├── models.py           # Defines and validates a Student
├── students.py         # Stores the student data
├── requirements.txt    # Lists project dependencies
├── README.md           # Explains the project
└── utils/
    ├── __init__.py     # Marks utils as a Python package
    └── helpers.py      # Contains reusable score functions
```

Each file has one main responsibility:

- `app.py` controls the flow of the program.
- `models.py` defines the validated `Student` data class.
- `students.py` keeps the data separate from the program logic.
- `utils/helpers.py` contains functions that can be reused elsewhere.
- `utils/__init__.py` allows Python to treat `utils` as a package.

This separation makes the project easier to read, test, and expand.

## Requirements

- Python 3.12 or newer
- No third-party packages

## Data Validation Feature

The project uses Python's standard-library `dataclasses` module. Every student
is created as a `Student` object and validated automatically:

- The name must be a non-empty string.
- The score must be an integer.
- The score must be between 0 and 100.

Invalid data is rejected with a clear error. For example,
`Student(name="Ada", score=120)` raises a `ValueError` because the score is
outside the accepted range. The data class is also immutable, which prevents
student records from being changed accidentally after creation.



## How to Run the Application

Install the listed dependencies (there are currently none):

```bash
python3 -m pip install -r requirements.txt
```

Run the application:

```bash
python3 app.py
```

Expected output:

```text
Student Scores
------------------------------
Ada: 84
Chidi: 92
Fatima: 76
Tunde: 88

Score Summary
------------------------------
Highest: Chidi (92)
Lowest: Fatima (76)
```

## How the Modules Work Together

1. `models.py` defines the rules for valid student data.
2. `students.py` creates the validated student list.
3. `app.py` sends that list to the functions in `utils/helpers.py`.
4. The helper functions use `max()` and `min()` to find the required students.
5. `app.py` prints the student list and summary.

If the student list is empty, the application displays a helpful message
instead of trying to calculate the highest and lowest scores.
