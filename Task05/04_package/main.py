from pathlib import Path
from attendance import (
    read_attendance,
    find_consecutive_absentees,
    display_report
)


def main():
    input_file = Path(__file__).parent / "attendance.txt"

    try:
        attendance = read_attendance(input_file)
        result = find_consecutive_absentees(attendance)
        display_report(result)

    except FileNotFoundError:
        print("Error: Attendance file not found.")


if __name__ == "__main__":
    main()