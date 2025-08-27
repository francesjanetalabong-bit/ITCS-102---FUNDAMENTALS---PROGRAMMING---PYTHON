name = input ("Enter username --> ")
password = input ("password --> ")

#print(username == 'francesjane21' )
#print(password == '123456789' )

if (name.lower() == "frances_jane") and (password.lower() == "123456789"):
	print("Access granted")
else:
	print("Access denied")