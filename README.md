# Ultimate-password-checker
Do you want to know if your password was ever hacked? try this piece of code!!!

This a application which can tell you if your password was hacked. And if it was hacked, how many times!!!

The application runs through command prompt:
1) Open your command prompt
2) Go to the directory were you have the Password_checker.py file
3) Run the command
		python/python3 Password_checker.py password/multiple passwords

Dont write password in any cotations

Example: 
          python Password_checker.py hello helloworld


Algorithm

1)Hash password using hashlib(python library)
2)Get hacked password database from password API
3)Match your password from hacked password database obtained from API

Here's the trick
	The application doesn't send your entire password to the API instead, It sends only first 5 characters of your hashed hexadecimal password.
  	And gets the list of all passwords from the API database which match the first 5 characters of your password. 
  	The rest of the password matching takes place locally on your system.
	Thus the API never receives your complete password.
