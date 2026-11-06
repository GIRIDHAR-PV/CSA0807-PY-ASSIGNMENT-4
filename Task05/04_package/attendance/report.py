def display_report(result):
    print("STUDENTS ABSENT FOR 3 CONSECUTIVE DAYS")
    print("--------------------------------------")

    if result:
        for register_number in result:
            print(register_number)
    else:
        print("No students found.")