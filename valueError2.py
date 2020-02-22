'''
Write a script that reads a string from STDIN and raise ValueError exception if the string has more than 10 characters or else prints the read string.
The message to user must be : "Input String contains more than 10 characters."
Use try ... except clauses. Print the error message inside except block.
Provide 'PythonIsAmazing' as input string while executing the string.
'''
word=input()

try:
	if len(word)>10:
		raise ValueError
except ValueError as e:
		print("Input String contains more than 10 characters.")
