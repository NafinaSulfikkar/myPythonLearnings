'''program to find the distance between two points'''
import math
class Point:
	def __init__(self,x,y,z):
		self.x=x
		self.y=y
		self.z=z
	def __str__(self):
		return "point : ({},{},{})".format(self.x,self.y,self.z)
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def getZ(self):
		return self.z
	def dist_btw_points(point1,point2):
		dist=math.sqrt((point2.getX()-point1.getX())**2
		+(point2.getY()-point1.getY())**2
		+ (point2.getZ()-point1.getZ())**2)
		return dist
p2 = Point(4, 5, 6)
p3 = Point(-2, -1, 4)

print(Point.dist_btw_points(p2,p3))
