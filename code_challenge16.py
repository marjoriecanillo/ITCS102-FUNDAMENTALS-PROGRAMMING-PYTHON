import os
import json

print("STUDENT INFORMATION SYSTEM")
print("--------------------------------")
student_records = {}

while True:
    print("SELECT FROM THE CHOICES BELOW.\nA - Add information\nB - Print all records\nC - Search a record\nD -Delete a record\nE - Edit a record\nF - Exit")
    choice = input("Your choice --> ").lower()
    if choice == 'a':
        print("ADDING STUDENT INFORMATION")
        print("--------------------------")
        student_id = input("Enter student id: ")
        first_name = input("Enter first name: ").upper()
        last_name = input("Enter last name: ").upper()
        course = input("Enter course: ").upper()
        email = input("Enter email: ")
        student_records[student_id] = [first_name, last_name, course, email]
        print("Student information added successfully.\n")
        os.system('cls') 
        continue
    elif choice == 'b':
        print("PRINTING STUDENT RECORDS")
        print("-----------------------")
        for id, records in student_records.items():
            print("-----------------------")
            print(f"Student ID: {id} : {records}")
            print("-----------------------")
        continue    
    elif choice == 'c':
        os.system('cls')
        print("SEARCH STUDENT RECORD")  
        print("---------------------")
        search_id = input("Enter student id to search: ")
        if search_id in student_records:
            print("---------------------")
            print("\nRECORD FOUND.\n")
            print("---------------------")
        else:
            print("---------------------")
            print("\nRECORD NOT FOUND.\n")
            print("---------------------")
        continue
    elif choice == 'd':
        print("DELETE STUDENT RECORD")  
        print("---------------------")
        search_id = input("Enter student id to delete: ")
        if search_id in student_records:
            print("---------------------")
            print("\nRECORD FOUND.\n")
            print("---------------------")
            for a in student_records[search_id]:
                print(f"-- {a}")
            student_records.pop(search_id)
            print("RECORD DELETED")
        else:
            print("---------------------")
            print("\nRECORD NOT FOUND.\n")
            print("---------------------")
        continue
    elif choice == 'e':
        os.system('cls')
        print("EDIT STUDENT RECORD")  
        print("---------------------")
        search_id = input("Enter student id to edit: ")
        if search_id in student_records:
            print("---------------------")
            print("\nRECORD FOUND.\n")
            print("---------------------")
            for a in student_records[search_id]:
                print(f"-- {a}")
            print("Enter new details:")
            first_name = input("Enter first name: ").upper()
            last_name = input("Enter last name: ").upper()
            course = input("Enter course: ").upper()
            email = input("Enter email: ")
            student_records[search_id] = [first_name, last_name, course, email]
            print("RECORD UPDATED")
             
        else:
            print("---------------------")
            print("\nRECORD NOT FOUND.\n")
            print("---------------------")
        continue

    elif choice == 'f':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
        continue
