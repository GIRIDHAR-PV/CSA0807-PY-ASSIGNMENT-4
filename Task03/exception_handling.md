# Task 3 – Exception Handling

## 3.1 Exception Handling Design

Exception handling is used to prevent the program from stopping when it encounters invalid attendance records.

The program uses the following exceptions:

- ValueError: Handles invalid values and incorrect data.
- FileNotFoundError: Handles missing input files.
- PermissionError: Handles files that cannot be accessed.
- InvalidRecord: A custom exception used for damaged attendance records.

## 3.2 Custom Exception

The InvalidRecord class is created by inheriting from the built-in Exception class.

It is raised when:
- A record does not contain exactly three fields.
- The register number is missing.
- The student name is missing.
- The attendance status is neither PRESENT nor ABSENT.

Invalid records are stored in a separate error log with their line numbers.

## 3.3 Try and Except Structure

The program uses nested try and except blocks.

- The outer try block handles file-related errors.
- The inner try block handles invalid attendance records.
- The finally block is not required because the with statement automatically closes the file.

## 3.4 Misuse Experiment

If all exceptions are handled using a broad except block, programming errors may be hidden.

For example:

try:
    number = int("abc")
except:
    print("Error")

This approach does not identify the exact error.

Handling specific exceptions makes the program easier to debug and maintain.

## 3.5 Function Implementation

The parse_line() function validates each attendance record and returns the register number, student name and attendance status.

The summarise() function calculates the total valid records, present count and absent count.

Both functions are separated to improve code readability, reuse and testing.

## 3.6 Result

The program successfully processes valid attendance records and rejects damaged records.

The attendance summary and error log are generated separately.