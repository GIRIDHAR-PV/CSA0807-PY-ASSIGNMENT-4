
# TASK 1 – FILE-PROCESSING DESIGN REVIEW

## Task 1.1 – Diagnose the Script

The original program has the following design deficiencies:

1. **Hard-coded file path:** The program uses a fixed file location. If the file is moved to another computer or folder, the program will fail with FileNotFoundError.

2. **File is never closed:** The file is opened without a with statement. This may leave the file resource occupied and cause problems when handling multiple files.

3. **Reading the entire file:** The read() method loads the complete file into memory. This can consume excessive memory when processing 50,000 or more records.

4. **Bare except with pass:** It hides all errors without identifying their causes. Invalid records are silently ignored, making it difficult to correct mistakes.

5. **Incorrect amount handling:** Using int() cannot process amounts containing paise, such as 1250.50. This causes ValueError.

6. **Repeated string concatenation:** Building the report using repeated + operations is inefficient for large reports.

7. **Empty lines:** Splitting the file using split("\n") may produce an empty record at the end, which can cause indexing errors.

8. **No rejected record tracking:** Invalid records are discarded without maintaining a record of rejected lines. This makes auditing difficult.

## Task 1.2 – Repair the Design

The corrected program is implemented in task1_2.py.

The program uses:
- A function that accepts the filename as a parameter.
- A with statement to open and close the file safely.
- Line-by-line reading to reduce memory usage.
- Decimal to process amounts containing paise accurately.
- Specific exceptions to handle invalid records.
- A list to store rejected records.
- A list to build the report efficiently.

## Task 1.3 – Design Defence

The corrected program is safer for processing 50,000 lines because it reads one line at a time instead of loading the entire file into memory. The with statement automatically closes the file after processing. Specific exception handling identifies invalid records, while the rejected-lines list maintains an audit record. Decimal ensures accurate financial calculations involving paise. These improvements make the program more reliable, memory-efficient and suitable for large files.

## Alternative Concept and Complexity Analysis

If read() or readlines() were used instead of line-by-line iteration, the entire file would be loaded into memory before processing.

### Solution using read()

The program could use:

data = file.read()

Then split the contents into individual lines and process each record.

### Time Complexity

Both approaches require O(n) time because every record must be processed once, where n represents the number of lines.

### Space Complexity

- read() or readlines(): O(file size), because the entire file is stored in memory.
- Line-by-line iteration: O(one line) for reading the input, excluding the report and rejected-record collections.

For a file containing 50,000 lines, line-by-line reading reduces input memory consumption and is more suitable for large files.
