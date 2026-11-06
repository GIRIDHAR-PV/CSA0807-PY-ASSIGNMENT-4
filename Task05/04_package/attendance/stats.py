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