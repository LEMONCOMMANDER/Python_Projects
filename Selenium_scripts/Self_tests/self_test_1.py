from selenium import webdriver
# "A Service class that is responsible for the starting and stopping of 'chromedriver'"
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # to hit enter and to type
# the following 2 imports allow us to introduce a wait period to ensure that a page has loaded and that the element could be found - we can also introduce timeouts
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# exception
from selenium.common.exceptions import TimeoutException
import sys
import time
import pytest
from selenium.common.exceptions import StaleElementReferenceException


''' STRUCTURE
1. go to goolge and search for website - srs acquiom 
2. click on website link and go to website
3. go to "our solutions"
4. click "deal dashboard"
5. click "see the full suite"
6. click "see it live"
7. log the contact phone number and the hours of operations from this page  
'''

# ----------------------------------------- VARIABLES -----------------------------------------
# ## SETUP
service = Service(executable_path=r"C:\Users\jibji\Documents\Code_Stuff\Python_Projects\chromedriver.exe")  # need to reinstall chrome driver
driver = webdriver.Chrome(service=service)  # service is a function of crhome that activates the crhomedriver
value_options = ["XPATH", "ID", "CLASS_NAME", "NAME", "CSS_SELECTOR", "LINK_TEXT", "PARTIAL_LINK_TEXT", "TAG_NAME"]
# ##
status_record = {}  # record of each element searched via condition_wait()
status_count = 1
google = "https://www.google.com/"
srs_search = 'https://www.google.com/search?q=srs+acquiom+home+page&sca_esv=a70b42618ebf6605&sca_upv=1&sxsrf=ADLYWIK_0oOo2Xi9BSe00qmL8C6q1dwmew%3A1725913043783&source=hp&ei=01ffZvCzLYzSp84P7Ou6uAI&iflsig=AL9hbdgAAAAAZt9l420zpC_yPAzPJisWRs6DXDdr6IJz&oq=srs+aquiom&gs_lp=Egdnd3Mtd2l6IgpzcnMgYXF1aW9tKgIIATIHECMYsQIYJzIHECMYsQIYJzIQEC4YgAQYsQMYxwEYChivATIHEAAYgAQYCjIHEAAYgAQYCjIHEAAYgAQYCjIHEAAYgAQYCjIHEAAYgAQYCjIHEAAYgAQYCjIHEAAYgAQYCkiKIlAAWP8RcAB4AJABAJgBgQKgAe0KqgEFMS43LjG4AQHIAQD4AQGYAgmgAq4LwgIKECMYgAQYJxiKBcICBBAjGCfCAhMQLhiABBgUGIcCGMcBGI4FGK8BwgIKEAAYgAQYQxiKBcICDRAuGIAEGLEDGEMYigXCAhAQABiABBixAxiDARgUGIcCwgIKEC4YgAQYQxiKBcICDhAuGIAEGLEDGIMBGIoFwgIWEC4YgAQYsQMYFBiHAhjHARiOBRivAcICEBAAGIAEGLEDGEMYgwEYigXCAg0QABiABBixAxhDGIoFwgIREC4YgAQYsQMYxwEYjgUYrwHCAggQABiABBixA8ICBRAAGIAEwgITEC4YgAQYsQMYFBiHAhjHARivAcICDRAuGIAEGNEDGMcBGAqYAwCSBwUwLjguMaAH8Wg&sclient=gws-wiz'

# ----------------------------------------- VARIABLES -----------------------------------------


# ----------------------------------------- WAIT FUNCTION -----------------------------------------
def condition_wait(search_type, value, fail_command="exit", wait_time=30):
    global status_count
    if search_type.upper() in value_options:
        try:
            # wait for chromedriver to load the html content, wait for 30 seconds... if something happens, continue, if no element is found, go to except block 
            WebDriverWait(driver, wait_time).until (# .until = "Calls the method provided with the driver as an argument until the return value does not evaluate to "False"
                EC.presence_of_element_located((getattr(By, search_type), value))   
                )
            status_record[f"{status_count}"] = "found element: " + f"{value}"
            print("run:" + f"{status_count}" + " found element ok")
            print("element is: " + f"{value}")
            print("")
            status_count += 1
            return_status = "ok"
            search_element = [search_type, value]
            return [return_status, search_element]
        except TimeoutException:
            print("on search #" + f'{status_count}' + ", " + f'{value}' + " not found")
            if fail_command == "next":
                # intention to log and run again where this function is called
                print("retry on " + f"{status_count}")
                status_count + 1 
                status_record[f"{status_count}"] = f'{value}' + " not found. User continue"
                return_status = "retry"
                return [return_status]
            else:
                print("user exit")
                search_element = [search_type, value]
                status_record[f"{status_count}"] = f"{value}" + " element not found, retry failed. EXIT"
                return_status = "fail"
                return [return_status, search_element, status_record]
    else:
        # if value is not a valid option - check value_options variable list 
        print("value error - bad input")
        status_record[f"{status_count}"] = f'{value}' + "value error - bad user input"
        return_status = "fail"
        search_element = [search_type, value]
        return [return_status, search_element, status_record]
    
    




# ----------------------------------------- STEP FUNCTIONS -----------------------------------------
'''step 1'''
def test_step1(): 
    print("step 1 STARTS")
    driver.get(google)  # goes to goolge
    current_search = condition_wait("ID", "APjFqb", "next")  # serach for google's search bar and returns the "return_value" status
    # this part can eventually be a method built into the condition_wait() function?
    if current_search[0] == "retry":
        current_search = condition_wait("ID", "APjFqb")  # search again and will quit if retry fails
    assert current_search[0] != "fail", "element was not found"
                                        # this part triggers if the assertion statement fails (aka there is an error)
                                        # assert condtion, "error message"
    
    google_search = driver.find_element(By.ID, 'APjFqb')
    google_search.send_keys("srs acquiom home page")  # searches for SRS Acquiom website 
    google_search.send_keys(Keys.ENTER)  # send_keys is a method from selenium.webdriver.common.keys import above 

    second_search = condition_wait("CSS_SELECTOR", "cite.tjvcx.GvPZzd.cHaqb", "next")  # including the name srs acquiom in the link
    if second_search[0] == "retry":
        second_search = condition_wait("CSS_SELECTOR", "cite.tjvcx.GvPZzd.cHaqb")  # search again and will quit if retry fails
    assert second_search[0] != "fail"
    srs_url = driver.find_element(By.CSS_SELECTOR, "cite.tjvcx.GvPZzd.cHaqb")
    assert srs_url.text == "https://www.srsacquiom.com"
    
    
    

    # if len(current_search) > 2:  # if the find element and retry fail:
    #     return_info = slice(1)
    #     return current_search[return_info]  # should return "search_element" and "status_record" 
    # else:  # if passes:
    #     return current_search[1]  # only returns search_element for testing purposes 


'''step 2'''
def test_step2():
    print('')
    print ("step 2 STARTS")
    current_search = condition_wait("CSS_SELECTOR", "cite.tjvcx.GvPZzd.cHaqb", "next")  # including the name srs acquiom in the link
    if current_search[0] == "retry":
        print("retry happened")
        current_search = condition_wait("CSS_SELECTOR", "cite.tjvcx.GvPZzd.cHaqb")  # search again and will quit if retry fails
    assert current_search[0] != "fail", "element not found"
    
    
    click_item = driver.find_element(By.CSS_SELECTOR, "cite.tjvcx.GvPZzd.cHaqb")  # finds first instance with "srs acquiom" in URL
    click_item.click()  # goes to srs aqcuiom website
    
    main_page = driver.find_element(By.CLASS_NAME, "home-page")
    carousell = driver.find_element(By.CSS_SELECTOR, "div.flex.flex-col.bg-neutral-200") 
    class_name = main_page.get_attribute('class')
    assert carousell.is_displayed() == True 
    assert main_page.is_displayed() == True
    assert "home-page" in class_name, "step 2 assert fails"
    
    current_url = driver.current_url
    assert current_url == "https://www.srsacquiom.com/", 'not on "SRS homepage"'
    
     
def test_step2_half():
    print("step 2.5 START")
    current_search = condition_wait("CSS_SELECTOR", '#onetrust-accept-btn-handler', "next")
    if current_search[0] == "retry":
        current_search = condition_wait("CSS_SELECTOR", '#onetrust-accept-btn-handler')
    
    assert current_search[0] != "fail", "element wasn't found"
    
    click_item = driver.find_element(By.CSS_SELECTOR, '#onetrust-accept-btn-handler')
    
    assert click_item.is_displayed() == True #if there, pass test and click
    
    click_item.click()
    time.sleep(1)
    
    try:
        
        assert click_item.is_displayed() == False, "something went wrong with the click on 'accept"
    
    except StaleElementReferenceException:
        print("stale element error happened")
        click_item = driver.find_elements(By.CSS_SELECTOR, '#onetrust-accept-btn-handler')
        
        assert len(click_item) == 0
    # time.sleep(2)
    


'''step 3 (and 4)'''
def test_step3_and_4():
    print('')
    print("step 3+4 START")
    current_url = driver.current_url
    assert current_url == "https://www.srsacquiom.com/", 'not on "SRS homepage"'
     
    current_search = condition_wait("CSS_SELECTOR", '#nav-toggle', "next") # makes sure the element is loaded - it is always in the html code
    if current_search[0] == "ok": #if page loaded ok...
        if driver.find_element(By.CSS_SELECTOR, '#nav-toggle').is_displayed() == True: # check if the hamburger menu is displayed...
            print("using the burger menu")
            click_item = driver.find_element(By.CSS_SELECTOR, '#nav-toggle') # if yes, target the element
            
            assert click_item.is_displayed() == True 
            
            click_item.click()  # and click on it (open the hamburger menu)
            time.sleep(1) # wait a second 
            second_search = condition_wait("CSS_SELECTOR", 'a.second-level-link:nth-child(1)') #load "our solution"
            if second_search[0] == "ok":  # if the next element, 'Our Solutions', is found
                second_click = driver.find_element(By.CSS_SELECTOR, 'a.second-level-link:nth-child(1)')
                
                assert second_click.is_displayed() == True, 'issue clicking on "Our Solutions"'
                
                time.sleep(1)
                second_click.click()  # click on the parent <a>
                third_search = condition_wait("CSS_SELECTOR", '#our-solutions-mobile > div:nth-child(2) > a:nth-child(4)')
                if third_search[0] == "ok":  # If our-solutions is found in the burger menu,
                    third_click = driver.find_element(By.CSS_SELECTOR, '#our-solutions-mobile > div:nth-child(2) > a:nth-child(4)')
                    scroll = ""
                    if third_click.is_displayed() == True:
                        # print('DISPLAYED AMD SCROLLED')
                        time.sleep(2)
                        #GPT assist 
                        # initial_position = driver.execute_script("return window.pageYOffset:")
                        driver.execute_script("arguments[0].scrollIntoView()", third_click) #scrolls to the element 
                        # new_position = driver.execute_script("return window.pageYOffset;")
                        # assert initial_position != new_position
                        scroll = "did scroll"
                        print("SCROLL TEST")
                        
                        assert scroll != "" #make sure the scroll script executed 
                        
                    time.sleep(1)
                    assert third_click.is_displayed() == True
                    third_click.click()  # click it
                
                assert third_search[0] != "fail", 'did not find "Deal Dashboard" element'
            assert second_search[0] != "fail", 'did not find the "Our Solutions" element'
        
        else: 
            if driver.find_element(By.CSS_SELECTOR, '#nav-toggle').is_displayed() == False: # if hamburger menu IS hidden...
                print ("Using the top menu")
                sub_search = condition_wait("CSS_SELECTOR", '#our-solutions-nav-link.dropdown-toggle-link', "next")  # check for the top version of "our solutions" element
                if sub_search[0] == "ok":
                    click_item = driver.find_element(By.CSS_SELECTOR, "#our-solutions-nav-link.dropdown-toggle-link") # locate html element 
                    click_item.get_attribute("id")
                    
                    assert 'our-solutions-nav-link' in click_item #checks name of element is correct
                    assert click_item.is_displayed() == True
                    
                    click_item.click()  # click on it 
                    time.sleep(2)
                    DD = 'body > nav > div.nav-drop-down.hidden.xl\:block.nav-dropdown.bg-green-1000.h-\[370px\].absolute.right-0.left-0.-mt-\[1px\] > div > div.our-solutions-nav-dropdown.hidden.absolute.right-0.left-0.flex.justify-between.items-center.lg\:gap-\[68px\].px-4.lg\:px-\[100px\].lg\:pt-\[70px\] > div.flex.gap-\[3px\].w-full > a:nth-child(4)'
                    #'.our-solutions-nav-dropdown > div:nth-child(2) > a:nth-child(4)'
                    second_search = condition_wait("CSS_SELECTOR", DD)
                    if second_search == "ok":
                        second_click = driver.find_element(By.CSS_SELECTOR, DD)
                        #.our-solutions-nav-dropdown > div:nth-child(2) > a:nth-child(4) > div:nth-child(1)
                        second_click.click()
                    return
                elif sub_search[0] == "retry":  # if not, look again...
                    sub_search = condition_wait("CSS_SELECTOR", '#our-solutions-nav-link.dropdown-toggle-link')
                    
                    assert sub_search[0] != "fail", 'did not find "Deal Dashboard" in desktop view dropdown'
   
    elif current_search[0] == "retry":
        current_search = condition_wait("CSS_SELECTOR", '#nav-toggle')
        
        assert current_search[0] != "fail", 'did not find desktop view "Our Solutions"'

    # if len(third_search) > 2:  # if the find element and retry fail:
    #     return_info = slice(1)
    #     return third_search[return_info]  # should return "search_element" and "status_record" 
    # else:  # if passes:
    #     return third_search[1]  # only returns search_element for testing purposes 
    
    current_url = driver.current_url
    assert current_url == "https://www.srsacquiom.com/solutions/m-a-dashboard/", 'not on "Deal Dashboard'


'''step 5'''
def test_step5():
    current_url = driver.current_url
    assert current_url == "https://www.srsacquiom.com/solutions/m-a-dashboard/", 'not on "Deal Dashboard"'
    
    #                  look for a tag with class name including min-w, and filter by 157px. Take the 3rd instance of this on the page 
    #                                                            ^^^^^^
    current_search = condition_wait("CSS_SELECTOR", 'a.min-w-\[157px\]:nth-child(3)', "next")  # search for "see the full suite"
    if current_search[0] == "retry":
        current_search = condition_wait("CSS_SELECTOR", 'a.min-w-\[157px\]:nth-child(3)')  # search again and will quit if retry fails
    
    assert current_search[0] != "fail", 'did not find "See Full Suite'
        
    click_item = driver.find_element(By.CSS_SELECTOR, 'a.min-w-\[157px\]:nth-child(3)')
    #gpt scroll test
    initial_position = driver.execute_script("return window.pageYOffset;")
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView()", click_item)
    time.sleep(1)
    new_position = driver.execute_script("return window.pageYOffset;")
    
    assert initial_position != new_position, "step 5 - no scroll"
    assert click_item.is_displayed() == True
    assert click_item.text == "SEE THE FULL SUITE", 'button text issue - "see the full suite"'
    
    click_item.click()
    
    # if len(current_search) > 2:  # if the find element and retry fail:
    #     return_info = slice(1)
    #     return current_search[return_info]  # should return "search_element" and "status_record" 
    # else:  # if passes:
    #     return current_search[1]  # only returns search_element for testing purposes 

    current_search = driver.current_url
    assert current_search == "https://www.srsacquiom.com/solutions/"
    
'''step 6'''
def test_step6():
    current_search = driver.current_url
    assert current_search == "https://www.srsacquiom.com/solutions/"
    
    current_search = condition_wait("CSS_SELECTOR", '.mb-10', 'next') #find "see it live"
    if current_search[0] == "retry":
        current_search = condition_wait("CSS_SELECTOR", '.mb-10')  # search again and will quit if retry fails
    
    assert current_search[0] != "fail", 'did not find "see it live"'
    
    click_item = driver.find_element(By.CSS_SELECTOR, '.mb-10')
    
    assert click_item.text == "SEE IT LIVE"
    assert click_item.is_displayed() == True
    
    time.sleep(1)
    click_item.click()
    
    # if len(current_search) > 2:  # if the find element and retry fail:
    #     return_info = slice(1)
    #     return current_search[return_info]  # should return "search_element" and "status_record" 
    # else:  # if passes:
    #     return current_search[1]  # only returns search_element for testing purposes 

    current_search = driver.current_url
    assert current_search == "https://www.srsacquiom.com/contact/", "not on contact url page"

'''step 7'''
# return information 
def test_step7():
    current_search = driver.current_url
    assert current_search == "https://www.srsacquiom.com/contact/", "not on contact url page"
    
    phone_number = driver.find_element(By.CSS_SELECTOR , 'div.gap-3:nth-child(1) > div:nth-child(2) > p:nth-child(2) > a:nth-child(1)').text
    op_hours = driver.find_element(By.CSS_SELECTOR, 'div.gap-3:nth-child(1) > div:nth-child(2) > p:nth-child(3)').text
    print(op_hours)
    
    
    assert phone_number == "303.222.2080", "wrong phone number - step 7"
    # assert op_hours == 
    
    
    
    # return [phone_number, op_hours]




# ----------------------------------------- APPLICATION -----------------------------------------

#can create seperate test files that import the functions - each one has a specific element that is retured, and can match the 
#statuses to understand the progression 


# def full_run():
#     # step1()
#     time.sleep(2)
#     step2()
#     step2_half()
#     step3_and_4()
#     step5()
#     step6()
#     results = step7()
#     phone_number = results[0]
#     op_hours = results[1]
#     print('')
#     print("the phone number of SRS Aquiom is: " + str(phone_number))
#     print("and")
#     print("the operating hours of SRS Aquiom is: ")
#     print(op_hours)
#     print('')
#     print("FINISHED...")
#     return([phone_number, op_hours]) 

