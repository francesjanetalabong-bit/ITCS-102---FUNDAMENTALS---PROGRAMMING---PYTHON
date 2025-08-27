from getpass import getpass
name = input ("Enter username --> ")
password = getpass ("Enter password --> ")

#print(username == 'francesjane21' )
#print(password == '123456789' )

uname = "francesjane21"
p_input = "123456789"

if (name.lower() ==uname) and (password.lower() == p_input):
	print("Access granted")
else:

	print("Access denied")
