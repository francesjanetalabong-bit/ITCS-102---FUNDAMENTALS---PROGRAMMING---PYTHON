#comments
#jeepney fare
#user would input their name
#if user is student , student discount must be applied
#20% discount on the student, if not student no discount

name = input("Input your name ---> ")
isStudent = input("Are you a student (Yes/No) --> ")
fare = eval(input("bayad --> "))

if isStudent.lower()== "yes":
	discount = fare * .2
	new_fare = fare - discount
	print("Hi" , name, "student discount"
	" Discounted fare is ", new_fare)
else: 
	print("Sorry ", name," you are not eligible for  student discount") 