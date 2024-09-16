"""called shapes in the video"""

import math

class Shapes:
    def area(self):
        pass
    def perimeter(self):
        pass
    
class Circle(Shapes):
    
    def __init__(self, radius):
        self.radius = radius # defines the objects "radius", through self.radius, to equal what is passed as the radius argument. 
                             # when an instance is created, self.radius is what will be referenced in that instance - SEE: circle_test.py test_area(self)
    
    def area(self):
        return math.pi * self.radius ** 2 # calls on the self.radius ^ | ** is to the power of (exponential)
    
    def perimeter(self):
        return 2 * math.pi * self.radius 
    

class Rectangle(Shapes):
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def __eq__(self, other): 
        # if this is not a rectangle, then return False. Otherwise, check if new rectangle == another instance 
        if not isinstance(other, Rectangle): # look up isnstance()
            return False
        
        return self.width == other.width and self.length == other.length # overwrites existing rectnalge dimension
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (self.length * 2) + (self.width * 2)
    
    