from pathlib import Path


def read_attendance(file_path):
    attendance = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue

            parts = line.strip().split(",")

            if len(parts) != 3:
                print("Invalid record at line", line_number)
                continue

            register_number = parts[0].strip()
            date = parts[1].strip()
            status = parts[2].strip().upper()

            if not register_number or not date or status not in ("P", "A"):
                print("Invalid record at line", line_number)
                continue

            attendance.setdefault(register_number, []).append((date, status))

    return attendance


def find_consecutive_absentees(attendance):
    result = []

    for register_number, records in sorted(attendance.items()):
        records.sort()
        consecutive = 0

        for date, status in records:
            if status == "A":
                consecutive += 1
            else:
                consecutive = 0

            if consecutive == 3:
                result.append(register_number)
                break

    return result


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