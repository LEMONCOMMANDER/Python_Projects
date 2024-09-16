import source.class_based as shapes

import pytest

import math 

'''              SETUP & TEAR DOWN  
.setup is a method inside class based testing that is designed to run "setup code" before each test is run. Runs at the beginning
of each test. Similarly, there is a teardown method that runs at the end of each test. Both of these methods need to be called as a 
function inside the test project to be implemented as part of the tests. 
'''


class TestCircle:
    
    def setup_method(self, method): # method here represents the method that will be run (the test, or class method 
                                     # which the setup method will be executed on).
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10) ##!! VARIABLE NAME IS self.circle
    
    
    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle
    
    
    # def test_one(self): 
    #     assert True    
    # the purpose of this code was to demonstrate the effects of the setup and teardown methods in the terminal. At the time, just a print statement for each


    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius  ** 2
        
    def perimeter_test(self):
        result = self.circle.perimeter()
        expected_result = 2 * math.pi * self.circle.radius
        assert result == expected_result



