student_records = {}

while True:
    print("select from options \nA - Add Student Information\nB - Print all Record\nC - Search Student Record\nD - Delete Student Record\nE - Edit Student Record\nF - Export Data\nG - Exit")

    choice = input("Your choice --> ").lower()



    if choice == 'a':
        print("Adding student information")
        print(" ----------------------")
        student_id = input("Key search for this student use this pattern(course-IDNO)--> ")

        first_name = input("Input your first name--> ")
        last_name = input("Input your last name--> ")
        course = input("input your course--> ")
        email = input("Input your email--> ")

        student_records [student_id] = [first_name, last_name, course, email]
        print("Data saved")

        continue

    elif choice =='b':
        print("Printing Student Records")

        for id,records in student_records.items():
            print(f"Student id {id} in Student Records {records}")
        continue
    elif choice =='c':
        print("Search Student Record")

        search_id = input("Input ID to search-->")

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("Record Found")

                for j in student_records[search_id]:
                    print(f"-- {j}")

            else:
                print("Record Not Found")
            break
    elif choice == 'd':
        print("Delete Existing Record")

        search_id = input("Input ID to search-->")
        if search_id in student_records.keys():
                print("Record Found")

        for j in student_records[search_id]:
                print(f"-- {j}")

        student_records.pop(search_id)
        print("Record Deleted")
        continue
    elif choice == 'e':
         print("Edit/Modify Student Record")

         search_id = input("Input ID to search-->")

    for id in student_records.keys():
            if search_id in student_records.keys():
                print("Record Found")

                for j in student_records[search_id]:
                    print(f"-- {j}")

                first_name = input("Input New Student first name--> ").upper()
                last_name = input("Input New Student last name--> ").upper()
                course = input("input New Student course--> ").upper()
                email = input("Input New Student email--> ").upper()
            else:
                 print("No Record Found")
            break
    continue


                


         