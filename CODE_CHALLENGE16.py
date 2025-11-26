import os
import json
os.system('cls')
print("STUDENT INFORMATION SYSTEM")
print("===========================")


student_records = {}

while True: 
    print("SELECT FROM THE OPTIONS BELOW")
    print("A-Add Information")
    print("B-Print All Record")
    print("C-Search a Student Record")
    print("D-Delete a Student Record")
    print("E-Edit a Student Record")
    print("F-Export Data")
    print("G-Import Record")
    print("X-Exit")
    choice = input("Your choice   ------>  ").lower()
    os.system('cls')
    if choice == 'a':

        print("ADDING STUDENT INFORMATION")
        print("----------------------------")
        student_id = input("Key search for this student information ID ------>").lower()

        first_name = input("Enter the student first name ---->").upper()
        last_name =input("Input student last name ------->").upper()
        course = input("Input Student Course------>").upper()
        email = input("Student email address -->")

        student_records[student_id] = [first_name, last_name, course, email]
        print("DATA SAVED")

        os.system('cls')
        continue
    
    elif choice =='b': 
        os.system('cls')
        print("PRINTING STUDENT RECORD")

        for id,record in student_records.items():
            print(f"STUDENT ID {id} in STUDENT RECORD {record}")
        continue

    elif choice =='c':
        os.system('cls')
        print("SEARCH STUDENT RECORD")
        print("=========================")

        search_id = input("Input ID to search ----> ")

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("=====================================")
                print("\n\nRECORD FOUND")
                print("=====================================")
                for i in student_records[search_id]:
                    print(f"-- {i}")
            else:
                print("=====================================")
                print("\n\n NO RECORD FOUND")
                print("=====================================")
            break
        continue

    elif choice == 'd':
        os.system('cls')
        print("DELETE EXISTING RECORD")
        print("=========================")

        search_id = input("Input ID to delete ----> ").lower()
        
        for id in student_records.keys():
            if search_id in student_records.keys():
                print("=====================================")
                print("\n\nRECORD FOUND")
                print("=====================================")
                for i in student_records[search_id]:
                    print(f"-- {i}")

                student_records.pop(search_id)
                print("RECORD DELETED")
            else:
                print("=====================================")
                print("\n\n NO RECORD FOUND")
                print("=====================================")
            break
        continue    

    elif choice == 'e':
        os.system('cls')
        print("EDIT/MODIFY STUDENT RECORD")
        print("=========================")

        search_id = input("Input ID to edit ----> ").lower()

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("=====================================")
                print("\n\nRECORD FOUND")
                print("=====================================")

                for i in student_records[search_id]:
                    print(f"-- {i}")
                

                first_name = input("Enter the student first name ---->").upper()
                last_name =input("Input student last name ------->").upper()
                course = input("Input Student Course------>").upper()
                email = input("Student email address -->").upper()

                student_records[search_id][0] = first_name
                student_records[search_id][1] = last_name
                student_records[search_id][2] = course
                student_records[search_id][3] =  email

                print("DATA UPDATED")
            
            else:
                print("=====================================")
                print("\n\nRECORED DELETED")
                print("=====================================")
            break
        continue 

    elif choice == 'f':
        os.system("cls")
        print("EXPORTING STUDENT RECORD")
        
        with open('student_record.json', 'w') as new_file:
            json.dump(student_records,new_file, indent=4)
    
        print("DATA EXPORTED TO JSON")

        continue 

    elif choice =='g':
        os.system('cls')
        print("Import Student Record")

        with open('student_record.json', 'r') as new_file:
            student_json = json.load(new_file)

        student_records = student_json
        print("DATA IMPORTED TO JSON")

        continue

    elif choice == 'x': 
        print("SYSTEM EXIT")
        break

    else:
         print("INVALID CHOICE, PLEASE RE-ENTER YOUR CHOICE")
        

        
