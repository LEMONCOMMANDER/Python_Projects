import source.fixture_based as shapes

import pytest #used for fixtures

import math 



''' NOTE on defining the class...
INTENTIONALLY, this file has no setup method where a rectangle is defined -- remember that [setup / teardown] is only for classes.
    Therefore it is established at the beginning of each test... which is not efficient. 

This could be solved with a class, similarly to the circle_test... but this file addresses how to do so with FIXTURES

The fixture is defined with the  @pytest.fixture  syntax and is then called as the parameter of the test functions. This takes
    the place of creating a new rectangle each time. I will leave the original statements commented out for display.
    
Many fixtures can be defined and used through the different tests. NOTE FIXTURES CAN BE GLOBAL NOTE 
    This means all your test projects can access the fixtures IF made global - a process called "conftesting"
           
           -- https://docs.pytest.org/en/stable/reference/fixtures.html
            
    A new file will be created called conftest.py - pytest will automatically discover fixtures in this document.
'''

# ----------------------------------------- Fixtures

# NOTE copying these fixtures to conftest.py --> everything will still work in this test.

# @pytest.fixture#        ||   see NOTE 4 
# def my_rectangle():
#     return shapes.Rectangle(10, 20)

# # NOTE second fixture requires a new shape -- see 35:29 in video  

# @pytest.fixture
# def second_rectangle():
#     shapes.Rectangle(5, 6)

# ------------------------------------------ Tests
def test_area(my_rectangle):
    # rectangle = shapes.Rectangle(10, 20) || REPLACED WITH FIXTURE
    
    assert my_rectangle.area() == my_rectangle.length * my_rectangle.width #rectangle > my_rectangle
    
def test_perimeter(my_rectangle):
    # rectangle = shapes.Rectangle(10, 20) || REPLACED WITH FIXTURE
    
    result = my_rectangle.perimeter() #rectangle > my_rectangle
    expected = (my_rectangle.length * 2) + (my_rectangle.width * 2) #rectangle > my_rectangle
    assert result == expected
    # this approach differs from the video but I wanted to get some extra reps in 
    
    
def test_not_equal(my_rectangle, second_rectangle):
    assert my_rectangle != second_rectangle
    