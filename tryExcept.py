try:
	a=2**4
	print("Ans: {}".format(a))
	b=pow(2,'hello')
	print("Ans: {}".format(b))
except TypeError as e:
	print("TypeError")

	#raise keyword
try:
	a=2
	b='hello'
	if not (isinstance(a,int) and isinstance(b,int)):
		raise TypeError('Both inputs must be integers.#raise')
	c=a**b
	print(c)
except TypeError as e:
	print(e)
	
	#user defined exception
class CustomError(Exception):
	def __init__(self,value):
		self.value=value
	def __str__(self):
		return str(self.value)
try:
    a = 2; b = 'hello'
    if not (isinstance(a, int) and isinstance(b, int)):
        raise CustomError('Two inputs must be integers.#CustomError')
    c = a**b
except CustomError as e:
    print(e)
	
	#finally
def divide(a,b):
	try:
		result=a/b
		print (result)
	except ZeroDivisionError:
		print ("Dividing by Zero")
	finally:
		print("Finally Clause.")
divide(10,0)

	#else
try:
    a = 14 / 7
except ZeroDivisionError:
    print('oops!!!')
else:
    print('First ELSE')
try:
    a = 14 / 0
except ZeroDivisionError:
    print('oops!!!')
else:
    print('Second ELSE')