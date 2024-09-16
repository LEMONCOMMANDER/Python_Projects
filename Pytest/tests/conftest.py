import pytest

import source.fixture_based as shapes

@pytest.fixture#        
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def second_rectangle():
    shapes.Rectangle(5, 6)