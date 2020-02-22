'''
Define the function isEven which returns True, if a given number is even and returns False, 
if the number is odd.

Execute the statement isEven(43) and display the output.


'''
def isEven(number):
	if number%2==0:
		return True
	else:
		return False
print(isEven(43))