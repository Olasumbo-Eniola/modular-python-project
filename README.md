# SEN 401 Student Score Application

The application displays a list of students
and identifies the students with the highest and lowest scores.

## Project Structure

```text
sen_401/
├── app.py              # Starts the application and displays the results
├── students.py         # Stores the student data
├── requirements.txt    # Lists project dependencies
├── README.md           # Explains the project
└── utils/
    ├── __init__.py     # Marks utils as a Python package
    └── helpers.py      # Contains reusable score functions
```

Each file has one main responsibility:

- `app.py` controls the flow of the program.
- `students.py` keeps the data separate from the program logic.
- `utils/helpers.py` contains functions that can be reused elsewhere.
- `utils/__init__.py` allows Python to treat `utils` as a package.

This separation makes the project easier to read, test, and expand.

## Requirements

- Python 3 or newer
- No third-party packages



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

1. `app.py` imports the student list from `students.py`.
2. It sends that list to the functions in `utils/helpers.py`.
3. The helper functions use `max()` and `min()` to find the required students.
4. `app.py` prints the student list and summary.

