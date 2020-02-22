'''
Write a script that handles opening a non-existing file, 'unknown_file.txt', and prints the message File not found. to the user.
Use try ... except clauses. Print the user message inside except clause.
'''

try:
	f=open('unknown_file.txt',"r")
except FileNotFoundError as e:
	print("File not found.")