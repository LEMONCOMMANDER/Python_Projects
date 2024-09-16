import self_test_1 as source
import pytest
import time

service = Service(executable_path=r"C:\Users\jibji\Documents\Code_Stuff\Python_Projects\chromedriver.exe")  # need to reinstall chrome driver
driver = webdriver.Chrome(service=service)  # service is a function of crhome that activates the crhomedriver

# def first_test():
#     element = source.step1(use = "yes") # step returns 2 things, get the second
#     print("element is: " + element[1])
#     # time.sleep(5)
#     assert element[1] == "APjFqb" #index is required after function 
    
# first_test()

def second_test():
    print("ok")
    x = 1 
    y = 1 
    assert x == y 