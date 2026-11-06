
import csv
from pathlib import Path


def process_attendance(input_folder, output_folder):
    attendance = {}
    error_log = []

    input_path = Path(input_folder)
    output_path = Path(output_folder)

    output_path.mkdir(parents=True, exist_ok=True)

    files = sorted(input_path.glob("*.txt"))

    if not files:
        print("No attendance files found.")
        return

    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for line_number, line in enumerate(file, start=1):
                    line = line.strip()

                    if not line:
                        continue

                    try:
                        parts = line.split(",")

                        if len(parts) != 3:
                            raise ValueError("Invalid number of fields")

                        register_number = parts[0].strip()
                        date = parts[1].strip()
                        status = parts[2].strip().upper()

                        if not register_number or not date:
                            raise ValueError("Missing register number or date")

                        if status not in ("P", "A"):
                            raise ValueError("Invalid attendance status")

                        if register_number not in attendance:
                            attendance[register_number] = {
                                "present": 0,
                                "absent": 0
                            }

                        if status == "P":
                            attendance[register_number]["present"] += 1
                        else:
                            attendance[register_number]["absent"] += 1

                    except ValueError as error:
                        error_log.append(
                            f"{file_path.name}, Line {line_number}: "
                            f"{line} - {error}"
                        )

        except (FileNotFoundError, PermissionError, UnicodeDecodeError) as error:
            error_log.append(f"{file_path.name}: {error}")

    summary_file = output_path / "attendance_summary.csv"
    below_75_file = output_path / "below_75.txt"
    error_file = output_path / "damaged_lines.txt"

    with open(summary_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Register Number",
            "Present",
            "Absent",
            "Attendance Percentage"
        ])

        for register_number, counts in sorted(attendance.items()):
            present = counts["present"]
            absent = counts["absent"]
            total = present + absent
            percentage = (present / total) * 100

            writer.writerow([
                register_number,
                present,
                absent,
                f"{percentage:.2f}%"
            ])

    with open(below_75_file, "w", encoding="utf-8") as file:
        file.write("STUDENTS BELOW 75% ATTENDANCE\n\n")

        for register_number, counts in sorted(attendance.items()):
            total = counts["present"] + counts["absent"]
            percentage = (counts["present"] / total) * 100

            if percentage < 75:
                file.write(
                    f"{register_number} - {percentage:.2f}%\n"
                )

    with open(error_file, "w", encoding="utf-8") as file:
        file.write("DAMAGED ATTENDANCE RECORDS\n\n")

        for error in error_log:
            file.write(error + "\n")

    print("ATTENDANCE PROCESSING COMPLETED")
    print("Total students:", len(attendance))
    print("Damaged records:", len(error_log))
    print("Summary saved:", summary_file)
    print("Below 75% report saved:", below_75_file)
    print("Error log saved:", error_file)


if __name__ == "__main__":
    base_folder = Path(__file__).parent

    process_attendance(
        base_folder / "input",
        base_folder / "output"
    )
