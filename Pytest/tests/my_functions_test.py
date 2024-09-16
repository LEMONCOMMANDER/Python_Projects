import pytest
import source.my_functions as my_functions

#SEE NOTE 2 on readme.txt for more details.


def test_add():
    result = my_functions.add(1, 4)
    assert result == 5

'''ASSERT
python assert is a debugging aid that tests a condition. IF the condition is True, the program continues on. IF the condition is False, 
an AssertionError is raised, which interrupts the flow of the program 
'''

def test_divide():
    result = my_functions.divide(10,5)
    result == 2
    
def test_divide_by_0():
    with pytest.raises(ZeroDivisionError): # without this, the following code returns an error "ZeroDivisionError"
        ''' obviously you can't divide a number by 0 - so there is an error for this. pytest allows you to check any errors raised using the
            .raises() method. The error you want to capture is then passed as an argument which specifies what error you are looking for.
        
                    result = my_functions.divide(10,0)  
                    assert True
            
            This code wihtout the the with pytest.raises will result in the ZeroDivisionError, and return as an error in pytest. Using
            the pytest.raises() option, we wll adjust our code to the following: 
        '''    
        
        my_functions.divide(10,0) # the function here actually FAILS... but our test is looking for the error that is presented when 
                                  # it fails, which is the ZeroDivisionError.  
                                  
        # AT THIS POINT, 17:20 IN THE VIDEO, WE ARE ALTERING THE DIVIDE() FUNCTION TO HANDLE THIS ERROR IN my_functions.py
        # added a "ValueError" which will return a different error than we are expecting, causing this to fail.
        
 
# WHAT ABOUT STRINGS?

def test_add_strings():
    result = my_functions.add("i like", " burgers")
    assert result == "i like burgers"        