# Task 2 – Biometric Attendance Processing

## 2.1 Data Model

The attendance system uses a dictionary to store attendance details for each student.

- Register number is used as the unique key.
- Present count stores the number of days marked Present.
- Absent count stores the number of days marked Absent.
- Attendance percentage is calculated using:

Attendance Percentage = (Present Days / Total Days) × 100

## 2.2 File Operations

- The pathlib module is used to locate the input and output folders.
- The glob() method is used to identify all attendance text files.
- Each file is opened using a with statement.
- The files are read line by line to reduce memory usage.
- The csv module is used to generate the attendance summary.
- Damaged records are saved with the filename and line number.

## 2.3 Pseudocode

1. Start the program.
2. Locate the input and output folders.
3. Find all text files in the input folder.
4. Create an empty attendance dictionary and error log.
5. Read each attendance file line by line.
6. Split each line into register number, date and status.
7. Validate the record.
8. If the record is valid, update the student's attendance count.
9. If the record is invalid, store its filename, line number and error.
10. Calculate the attendance percentage for every student.
11. Generate the attendance summary CSV file.
12. Generate a separate report for students below 75%.
13. Save all damaged records in an error log.
14. Display the processing results.
15. Stop the program.

## 2.4 Trace and Expected Results

The program processes three daily attendance files.

| Register Number | Present | Absent | Percentage |
|---|---:|---:|---:|
| 192311001 | 3 | 0 | 100% |
| 192311002 | 1 | 1 | 50% |
| 192311003 | 2 | 1 | 66.67% |

Students below 75% attendance:
- 192311002
- 192311003

The invalid status `L` in day03.txt is rejected and recorded in the damaged records file.

## 2.5 Alternative Approach and Complexity

An alternative approach is to read all attendance records into a list before processing them.

Let:
- f = Number of files
- l = Average number of lines in each file

Reading and processing all records takes O(f × l) time.

Reading files line by line also takes O(f × l) time, but requires less temporary memory because the entire file is not loaded at once.

The dictionary provides efficient average O(1) lookup for each student's attendance record.