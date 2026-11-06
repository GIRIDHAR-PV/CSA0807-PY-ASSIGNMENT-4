from pathlib import Path


def process_records(input_file, output_file, error_file):
    valid_records = []
    errors = []

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        raise ValueError("Expected 3 fields")

                    register_number = parts[0].strip()
                    name = parts[1].strip()
                    marks = int(parts[2].strip())

                    if not register_number or not name:
                        raise ValueError("Missing register number or name")

                    if marks < 0 or marks > 100:
                        raise ValueError("Marks must be between 0 and 100")

                    valid_records.append(
                        f"{register_number},{name},{marks}"
                    )

                except ValueError as error:
                    errors.append(
                        f"Line {line_number}: {error} - {line.strip()}"
                    )

        with open(output_file, "a", encoding="utf-8") as file:
            for record in valid_records:
                file.write(record + "\n")

        with open(error_file, "a", encoding="utf-8") as file:
            for error in errors:
                file.write(error + "\n")

        print("FILE PROCESSING COMPLETED")
        print("Valid records:", len(valid_records))
        print("Damaged records:", len(errors))
        print("Output saved:", output_file)
        print("Error log saved:", error_file)

    except FileNotFoundError:
        print("Error: Input file not found.")

    except PermissionError:
        print("Error: Permission denied.")


if __name__ == "__main__":
    base_folder = Path(__file__).parent

    process_records(
        base_folder / "input" / "student_records.txt",
        base_folder / "output" / "valid_records.txt",
        base_folder / "output" / "error_log.txt"
    )