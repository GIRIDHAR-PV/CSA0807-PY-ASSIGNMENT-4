from pathlib import Path
from reader import read_attendance
from stats import find_consecutive_absentees


def main():
    input_file = Path(__file__).parent / "attendance.txt"

    try:
        attendance = read_attendance(input_file)
        result = find_consecutive_absentees(attendance)

        print("STUDENTS ABSENT FOR 3 CONSECUTIVE DAYS")
        print("--------------------------------------")

        if result:
            for register_number in result:
                print(register_number)
        else:
            print("No students found.")

    except FileNotFoundError:
        print("Error: Attendance file not found.")


if __name__ == "__main__":
    main()