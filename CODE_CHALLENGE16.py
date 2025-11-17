import os
print("STUDENT INFORMATION SYSTEM")
print("===========================")





student_records = {}

while True: 
    print("SELECT FROM THE OPTIONS BELOW\n A-add information,\n B-search a-record \n C-delete\n D-modify a record\n P-Print data \n E-exit")

    choice = input("Your choice   ------>  ").lower()

    if choice == 'a':
        print("ADDING STUDENT INFORMATION")
        print("----------------------------")
        search_code = input("Key search for this studentinformation ------>")

        first_name = input("Enter the student first name ---->")
        last_name =input("Input student last name ------->")
        course = input("Input Student Course------>")
        email = input("Student email address -->")
        isSingle =input("Are you single (True or False) ---->")

        student_records = {search_code : [first_name, last_name, course, email]}
        print("DATA SAVED")

        os.system('cls')
        continue

    elif choice =='b': 
        os.system('cls')
        code = input("Inputn search code --->")

        for j in student_records.keys():
            if code in student_records.keys():
                print("RECORD FOUND")

                print('RECORDS ' )
                print('------------')
                for i in student_records[code]:
                    print(i)

            else: 
                print("NO RECORD FOUND")
        # os.syste
        continue
    elif choice =='c':
        
        