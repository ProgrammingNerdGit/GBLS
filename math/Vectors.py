import math
import numpy as np
class _vector:
	def checkAndChange(self,n,b,operation):
		if(type(n) == type(vector2(0,0))):
			if(type(b) == type(vector2(0,0))):
				return b
			else:
				if(type(b) == type(1) or type(b) == type(1.1)):
					return vector2(b,b)
				else:
					raise Exception(f"cant do type {type(vector2)} {operation} {type(b)}")
		elif(type(n) == type(vector3(0,0,0))):
			if(type(b) == type(vector3(0,0,0))):
				return b
			else:
				if(type(b) == type(1) or type(b) == type(1.1)):
					return vector3(b,b,b)
				else:
					raise Exception(f"cant do type {type(vector3)} {operation} {type(b)}")
		else:
			if(type(b) == type(vectorN(0)) and len(b.axis) == len(n.axis)):
				return b
			else:
				try:
					if(len(b.axis) != len(n.axis)):
						raise Exception(f"cant {operation} vector length of {len(n.axis)} and {len(b.axis)}")
				except:
					pass
				if(type(b) == type(1) or type(b) == type(0.1)):
					res = []
					for i in range(len(n.axis)):
						res.append(b)
					return vectorN(raw=res)
				else:
					raise Exception(f"cant do type {type(vectorN(0))} {operation} {type(b)}")

class vector2(_vector):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __add__(self,b):
		b = self.checkAndChange(self,b,"+")
		return(vector2(self.x+b.x,self.y+b.y))
	def __sub__(self,b):
		b = self.checkAndChange(self,b,"-")
		return(vector2(self.x-b.x,self.y-b.y))
	def __mul__(self,b):
		b = self.checkAndChange(self,b,"*")
		return(vector2(self.x*b.x,self.y*b.y))
	def __mod__(self,b):
		b = self.checkAndChange(self,b,"%")
		return(vector2(self.x%b.x,self.y%b.y))
	def __truediv__(self,b):
		b = self.checkAndChange(self,b,"/")
		return(vector2(self.x/b.x,self.y/b.y))
	def __pow__(self,b):
		b = self.checkAndChange(self,b,"**")
		return(vector2(self.x**b.x,self.y**b.y))
	def __str__(self):
		return f"({self.x},{self.y})"
	def __repr__(self):
		return f"({self.x},{self.y})"


class vector3(_vector):
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
	def __add__(self,b):
		b = self.checkAndChange(self,b,"+")
		return(vector3(self.x+b.x,self.y+b.y,self.z+b.z))
	def __sub__(self,b):
		b = self.checkAndChange(self,b,"-")
		return(vector3(self.x-b.x,self.y-b.y,self.z-b.z))
	def __mul__(self,b):
		b = self.checkAndChange(self,b,"*")
		return(vector3(self.x*b.x,self.y*b.y,self.z*b.z))
	def __mod__(self,b):
		b = self.checkAndChange(self,b,"%")
		return(vector3(self.x%b.x,self.y%b.y,self.z%b.z))
	def __truediv__(self,b):
		b = self.checkAndChange(self,b,"/")
		return(vector3(self.x/b.x,self.y/b.y,self.z/b.z))
	def __pow__(self,b):
		b = self.checkAndChange(self,b,"**")
		return(vector3(self.x**b.x,self.y**b.y,self.z**b.z))
	def __str__(self):
		return f"({self.x},{self.y},{self.z})"
	def __repr__(self):
		return f"({self.x},{self.y},{self.z})"

class vectorN(_vector):
	def __init__(self,*args,**kwargs):
		if("raw" in kwargs.keys()):
			self.axis = kwargs.get("raw")
		else:
			self.axis = list(args)
	def __add__(self,b):
		b = self.checkAndChange(self,b,"+")
		res = []
		for i in range(len(self.axis)):
			res.append(self.axis[i]+b.axis[i])
		return vectorN(raw=res)
	def __sub__(self,b):
		b = self.checkAndChange(self,b,"-")
		res = []
		for i in range(len(self.axis)):
			res.append(self.axis[i]-b.axis[i])
		return vectorN(raw=res)
	def __mul__(self,b):
		b = self.checkAndChange(self,b,"*")
		res = []
		for i in range(len(self.axis)):
			res.append(self.axis[i]*b.axis[i])
		return vectorN(raw=res)
	def __mod__(self,b):
		b = self.checkAndChange(self,b,"%")
		res = []
		for i in range(len(self.axis)):
			res.append(self.axis[i]%b.axis[i])
		return vectorN(raw=res)
	def __truediv__(self,b):
		b = self.checkAndChange(self,b,"/")
		res = []
		for i in range(len(self.axis)):
			res.append(self.axis[i]/b.axis[i])
		return vectorN(raw=res)
	def __pow__(self,b):
		b = self.checkAndChange(self,b,"**")
		res = []
		for i in range(len(self.axis)):
			res.append(self.axis[i]**b.axis[i])
		return vectorN(raw=res)

	def __str__(self):
		return str(tuple(self.axis))
	def __repr__(self):
		return str(tuple(self.axis))
#y=mx+b
def lerp2(a,b,numPoints):
	m = (b.y-a.y)/(b.x-a.x)
	B = a.y-(m*a.x)
	points = []
	for i in np.linspace(a.x,b.x,numPoints):
		points.append(vector2(i,m*i+B))

	return points
def magnitude(a,b):
    if(type(a) == type(vector2(0,0))): a = vectorN(a.x,a.y)
    if(type(b) == type(vector2(0,0))): b = vectorN(b.x,b.y)
    if(type(a) == type(vector3(0,0,0))): a = vectorN(a.x,a.y,a.z)
    if(type(b) == type(vector3(0,0,0))): b = vectorN(b.x,b.y,b.z)
    
    return sum(abs(a.axis[i]-b.axis[i])**2 for i in range(len(a.axis)))**0.5
