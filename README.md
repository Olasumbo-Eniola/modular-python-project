# SEN 401 Student Score Application

The application displays a formatted student score report and calculates the
highest, lowest, average, and median scores.

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
- `students.py` stores immutable default records and provides functions that
  create fresh, validated student lists.
- `utils/helpers.py` contains functions that can be reused elsewhere.
- `utils/__init__.py` allows Python to treat `utils` as a package.

This separation makes the project easier to read, test, and expand.

The raw sample data is stored in `DEFAULT_STUDENT_RECORDS`. The
`create_students()` function converts any compatible records into validated
objects, while `get_default_students()` returns a fresh list for the demo. This
prevents one part of the application from accidentally changing the original
data used elsewhere.

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

## Reporting Features

The console output uses aligned columns so the student data is easier to scan.
The summary includes:

- Number of students
- Highest score
- Lowest score
- Average score
- Median score

The average and median are calculated with Python's standard-library
`statistics` module. The median is the middle score after the scores have been
arranged in order. When there are two middle scores, their average is used.


## How to Run the Application

Install the listed dependencies (there are currently none):

```bash
python3 -m pip install -r requirements.txt
```

Run the application:

```bash
python3 app.py
```

## FastAPI

Install dependencies and start the API:

```bash
python3 -m pip install -r requirements.txt
uvicorn api:app --reload --port 8000
```

Open `http://localhost:8000/docs` for the interactive API documentation.
Available routes are `GET /health`, `GET /students`,
`GET /students/summary`, and `POST /students`.

Expected output:

```text
======================================
         STUDENT SCORE REPORT         
======================================
No.  Student                     Score
--------------------------------------
1    Ada                            84
2    Chidi                          92
3    Fatima                         76
4    Tunde                          88
--------------------------------------
            SCORE SUMMARY             
--------------------------------------
Number of students:                  4
Highest score:              92 (Chidi)
Lowest score:               76 (Fatima)
Average score:                   85.00
Median score:                    86.00
======================================
```

## How the Modules Work Together

1. `models.py` defines the rules for valid student data.
2. `students.py` stores the default records and creates a fresh validated list.
3. `app.py` sends that list to the functions in `utils/helpers.py`.
4. The helper functions calculate the score statistics.
5. `app.py` prints the student list and summary.

If the student list is empty, the application displays a helpful message
instead of trying to calculate the highest and lowest scores.
