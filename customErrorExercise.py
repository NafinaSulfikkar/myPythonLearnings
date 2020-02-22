'''
Define a class Circle, whose objects are initialized with radius as it's attribute.

Ensure that the object creation raises RadiusInputError, a user defined exception, when the input radius is not a number.

Use try ... except clauses.

Create a Circle c1 using the statement c1 = Circle('hello'), and execute the script.

The error message "'hello' is not a number" should be displayed to user.
'''
class RadiusInputError(Exception):
		def __init__(self,value):
			self.value=value
		def __str__(self):
			return str(self.value)
class Circle:
	def __init__(self,radius):
		self.radius=radius
		try:
			if not(isinstance(radius,int)):
				raise RadiusInputError("'{}' is not a number".format(radius))
		except RadiusInputError as e:
			print(e)
c1 = Circle('hello')