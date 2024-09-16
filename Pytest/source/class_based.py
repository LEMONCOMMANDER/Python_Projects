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
    
    