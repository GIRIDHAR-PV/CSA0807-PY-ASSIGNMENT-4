from pathlib import Path


def main():
    input_file = Path(__file__).parent / "attendance.txt"

    attendance = {}

    try:
        with open(input_file, "r", encoding="utf-8") as file:
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

                if register_number not in attendance:
                    attendance[register_number] = []

                attendance[register_number].append((date, status))

        print("STUDENTS ABSENT FOR 3 CONSECUTIVE DAYS")
        print("--------------------------------------")

        found = False

        for register_number, records in sorted(attendance.items()):
            records.sort()

            consecutive = 0

            for date, status in records:
                if status == "A":
                    consecutive += 1
                else:
                    consecutive = 0

                if consecutive == 3:
                    print(register_number)
                    found = True
                    break

        if not found:
            print("No students found.")

    except FileNotFoundError:
        print("Error: Attendance file not found.")


if __name__ == "__main__":
    main()