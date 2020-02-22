'''Write a script that reads an integer from STDIN and raise ValueError exception if the number is not between 0 and 100.

The message to user must be : "Input integer value must be between 0 and 100."

Use try... except clauses. Specify the error message inside except clause.

Provide 200 as input while executing the script'''

number=int(input())
try:
	if not (number<0 and number>100):
		raise ValueError
except ValueError as e:
	print("Input integer value must be between 0 and 100.")
	