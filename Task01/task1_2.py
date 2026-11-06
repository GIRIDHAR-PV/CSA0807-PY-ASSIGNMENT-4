
from decimal import Decimal, InvalidOperation
from pathlib import Path


def process_mess_file(file_name):
    total = Decimal("0.00")
    report = []
    rejected_lines = []

    with open(file_name, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            try:
                parts = line.split(",")

                if len(parts) != 3:
                    raise ValueError("Expected 3 fields")

                register_number = parts[0].strip()
                name = parts[1].strip()
                amount = Decimal(parts[2].strip())

                if not register_number or not name:
                    raise ValueError("Empty register number or name")

                if amount < 0:
                    raise ValueError("Negative amount")

                total += amount
                report.append(f"{register_number} - {name} - {amount:.2f}")

            except (ValueError, InvalidOperation) as error:
                rejected_lines.append(
                    (line_number, line, str(error))
                )

    return report, total, rejected_lines


def main():
    base_folder = Path(__file__).parent
    file_name = base_folder / "input" / "mess_oct.txt"

    try:
        report, total, rejected = process_mess_file(file_name)

        print("HOSTEL MESS BILL REPORT")
        print("------------------------------")

        for item in report:
            print(item)

        print("------------------------------")
        print("Total Amount:", total)

        print("\nRejected Lines:")

        if rejected:
            for item in rejected:
                print(item)
        else:
            print("No rejected lines")

        output_file = base_folder / "output" / "mess_report.txt"

        with open(output_file, "w", encoding="utf-8") as file:
            file.write("HOSTEL MESS BILL REPORT\n")
            file.write("------------------------------\n")

            for item in report:
                file.write(item + "\n")

            file.write("------------------------------\n")
            file.write(f"Total Amount: {total}\n")
            file.write("\nRejected Lines:\n")

            for item in rejected:
                file.write(str(item) + "\n")

        print("\nReport saved successfully.")

    except FileNotFoundError:
        print("Error: Input file not found.")

    except PermissionError:
        print("Error: Permission denied.")


if __name__ == "__main__":
    main()
