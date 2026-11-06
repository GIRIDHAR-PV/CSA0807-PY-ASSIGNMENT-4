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