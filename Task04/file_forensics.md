# Task 4 – File and Exception Forensics

## 4.1 File Opening Modes

The program uses different file modes for different operations.

- Read mode (`r`) reads the input records.
- Append mode (`a`) adds valid records to the output file.
- Append mode preserves existing records instead of deleting them.

## 4.2 Newline Handling

The write() function does not automatically add a new line.

Therefore, the program uses "\n" after each record to ensure that every record appears on a separate line.

## 4.3 With Statement

The with statement is used to open files safely.

It automatically closes the file after the operation is completed, even when an exception occurs.

## 4.4 Error Logging

Invalid records are stored in a separate error log.

The error log contains the line number and reason for rejection.

This helps identify and correct damaged records without stopping the entire program.

## 4.5 Try and Finally

An alternative approach is to use try and finally to close files manually.

The finally block executes whether an exception occurs or not.

However, the with statement is simpler and reduces the possibility of forgetting to close a file.

## 4.6 Result

The program successfully processes valid student records, appends them to the output file and records invalid entries separately.