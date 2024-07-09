# Exercise Name:
# 	09-OOP-Demo
# Description:
# 	Create a class and demonstrate how @property decorator is used

#Program to find the area of a circle

class Circle:
    def __init__(self,radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2
    
    @property
    def area(self):
        return 3.14 * self.radius * self.radius
    
    # @diameter.setter
    # def diameter(self, diameter):
    #     self.radius = diameter/2

c1 = Circle(7)
# c1.diameter = 12
print(f"Radius of the circle : {c1.radius}")
print(f"Diameter of the circle : {c1.diameter}")
print(f"Area of the circle : {c1.area}")

#commented code is just to demonstrate the use setters, by setting the diameter directly and taking tha radius from it