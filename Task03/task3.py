from pathlib import Path


class InvalidRecord(Exception):
    pass


def parse_line(line):
    parts = line.strip().split(",")

    if len(parts) != 3:
        raise InvalidRecord("Record must contain 3 fields")

    register_number = parts[0].strip()
    name = parts[1].strip()
    status = parts[2].strip().upper()

    if not register_number or not name:
        raise InvalidRecord("Register number or name is missing")

    if status not in ("PRESENT", "ABSENT"):
        raise InvalidRecord("Invalid attendance status")

    return register_number, name, status


def summarise(records):
    total = len(records)
    present = sum(1 for record in records if record[2] == "PRESENT")
    absent = total - present

    return total, present, absent


def main():
    base_folder = Path(__file__).parent
    input_file = base_folder / "input" / "attendance.txt"
    output_file = base_folder / "output" / "attendance_summary.txt"
    error_file = base_folder / "output" / "error_log.txt"

    records = []
    errors = []

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if not line.strip():
                    continue

                try:
                    record = parse_line(line)
                    records.append(record)

                except InvalidRecord as error:
                    errors.append(f"Line {line_number}: {error} - {line.strip()}")

        total, present, absent = summarise(records)

        with open(output_file, "w", encoding="utf-8") as file:
            file.write("ATTENDANCE SUMMARY\n")
            file.write(f"Total valid records: {total}\n")
            file.write(f"Present: {present}\n")
            file.write(f"Absent: {absent}\n")

        with open(error_file, "w", encoding="utf-8") as file:
            file.write("ERROR LOG\n")
            for error in errors:
                file.write(error + "\n")

        print("ATTENDANCE PROCESSING COMPLETED")
        print("Total valid records:", total)
        print("Present:", present)
        print("Absent:", absent)
        print("Damaged records:", len(errors))
        print("Summary saved:", output_file)
        print("Error log saved:", error_file)

    except FileNotFoundError:
        print("Error: Input file not found.")

    except PermissionError:
        print("Error: Permission denied.")


if __name__ == "__main__":
    main()