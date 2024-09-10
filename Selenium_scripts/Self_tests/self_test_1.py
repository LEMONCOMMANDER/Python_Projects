from selenium import webdriver
#"A Service class that is responsible for the starting and stopping of 'chromedriver'"
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #to hit enter and to type
# the following 2 imports allow us to introduce a wait period to ensure that a page has loaded and that the element could be found - we can also introduce timeouts
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#exception
from selenium.common.exceptions import TimeoutException
import sys


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
### SETUP
service = Service(executable_path="/Users/lemonlord/Documents/Code_Stuff/Selenium_Web_Drivers/chromedriver")
driver = webdriver.Chrome(service=service) #service is a function of crhome that activates the crhomedriver
value_options = ["XPATH", "ID", "CLASS_NAME", "NAME", "CSS_SELECTOR", "LINK_TEXT", "PARTIAL_LINK_TEXT", "TAG_NAME"]
###
status_record =  {} #record of each element searched via condition_wait()
status_count = 1
google = "https://www.google.com/"
srs_search = 'https://www.google.com/search?q=srs+acquiom+home+page&sca_esv=a70b42618ebf6605&sca_upv=1&sxsrf=ADLYWIK_0oOo2Xi9BSe00qmL8C6q1dwmew%3A1725913043783&source=hp&ei=01ffZvCzLYzSp84P7Ou6uAI&iflsig=AL9hbdgAAAAAZt9l420zpC_yPAzPJisWRs6DXDdr6IJz&oq=srs+aquiom&gs_lp=Egdnd3Mtd2l6IgpzcnMgYXF1aW9tKgIIATIHECMYsQIYJzIHECMYsQIYJzIQEC4YgAQYsQMYxwEYChivATIHEAAYgAQYCjIHEAAYgAQYCjIHEAAYgAQYCjIHEAAYgAQYCjIHEAAYgAQYCjIHEAAYgAQYCjIHEAAYgAQYCkiKIlAAWP8RcAB4AJABAJgBgQKgAe0KqgEFMS43LjG4AQHIAQD4AQGYAgmgAq4LwgIKECMYgAQYJxiKBcICBBAjGCfCAhMQLhiABBgUGIcCGMcBGI4FGK8BwgIKEAAYgAQYQxiKBcICDRAuGIAEGLEDGEMYigXCAhAQABiABBixAxiDARgUGIcCwgIKEC4YgAQYQxiKBcICDhAuGIAEGLEDGIMBGIoFwgIWEC4YgAQYsQMYFBiHAhjHARiOBRivAcICEBAAGIAEGLEDGEMYgwEYigXCAg0QABiABBixAxhDGIoFwgIREC4YgAQYsQMYxwEYjgUYrwHCAggQABiABBixA8ICBRAAGIAEwgITEC4YgAQYsQMYFBiHAhjHARivAcICDRAuGIAEGNEDGMcBGAqYAwCSBwUwLjguMaAH8Wg&sclient=gws-wiz'


# ----------------------------------------- VARIABLES -----------------------------------------

# ----------------------------------------- WAIT FUNCTION -----------------------------------------
def condition_wait(search_type, value, fail_command="exit", wait_time=30):
    global status_count
    if value.upper() in value_options:
        try:
            #wait for chromedriver to load the html content, wait for 30 seconds... if something happens, continue, if no element is found, go to except block 
            WebDriverWait(driver, wait_time).until ( # .until = "Calls the method provided with the driver as an argument until the return value does not evaluate to "False"
                EC.presence_of_element_located((getattr(By, search_type), value))   
                )
            status_record[f"{status_count}"] = "found element: " + f"{value}"
            status_count += 1
            return_status = "ok"
            search_element = [search_type, value]
            return [return_status, search_element]
        except TimeoutException:
            print("on search #" + f'{status_count}' + ", " + f'{value}' + " not found")
            if fail_command == "next":
                #intention to log and run again where this function is called 
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
        #if value is not a valid option - check value_options variable list 
        print("value error - bad input")
        status_record[f"{status_count}"] = f'{value}' + "value error - bad user input"
        return_status = "fail"
        return [return_status, search_element, status_record]


# ----------------------------------------- STEP FUNCTIONS -----------------------------------------
'''step 1'''
def step1(url = google):
    driver.get(google) #goes to goolge
    current_search = condition_wait("ID","APjFqb","next") #serach for google's search bar and returns the "return_value" status
    #this part can eventually be a method built into the condition_wait() function?
    if current_search[0] == "retry":
        current_search = condition_wait("ID","APjFqb") #search again and will quit if retry fails
    elif current_search[0] == "fail":
        sys.exit("broke at 1st step")
    
    google_search = driver.find_element(By.ID, 'APjFqb')
    google_search.send_keys("srs acquiom home page") #searches for SRS Acquiom website 
    google_search.send_keys(Keys.ENTER) #send_keys is a method from selenium.webdriver.common.keys import above 

    if len(current_search) > 2: #if the find element and retry fail:
        return_info = slice(1)
        return current_search[return_info] #should return "search_element" and "status_record" 
    else: #if passes:
        return current_search[1] #only returns search_element for testing purposes 

'''step 2'''
def step2(url = srs_search):
    current_search = condition_wait("PARTIAL_LINK_TEXT", "srsacquiom", "next") #including the name srs acquiom in the link
    if current_search[0] == "retry":
        current_search = condition_wait("PARTIAL_LINK_TEXT", "srsacquiom") #search again and will quit if retry fails
    elif current_search[0] == "fail":
        sys.exit("broke at 2nd step")
    
    click_item = driver.find_element(By.PARTIAL_LINK_TEXT, "srsacquiom") #finds first instance with "srs acquiom" in URL
    click_item.click() #goes to srs aqcuiom website
    
    if len(current_search) > 2: #if the find element and retry fail:
        return_info = slice(1)
        return current_search[return_info] #should return "search_element" and "status_record" 
    else: #if passes:
        return current_search[1] #only returns search_element for testing purposes 

'''step 3 (and 4)'''
def step3_and_4(url = 'https://www.srsacquiom.com/'):
    #have to check for hamburger menu becuase of resize
    current_search = condition_wait("CLASS_NAME","hamburger-box", "next")
    if current_search[0] == "ok": #if hamburger menu is found initially 
        click_item = driver.find_element(By.CLASS_NAME, "hamburger-box")
        click_item.click() #opens the hamburger menu
        second_search = condition_wait("XPATH", '//*[@id="nav-menu-mobile-container"]/section[1]/div[1]/div[1]/div/a[1]/svg')
        if second_search == "ok": #if the next element, 'Our Solutions', is found
            second_click = driver.find_element(By.XPATH, '//*[@id="nav-menu-mobile-container"]/section[1]/div[1]/div[1]/div/a[1]/svg')
            second_click.click() #click on the arrow to get to the sub-menu
            third_search = condition_wait("XPATH",'//*[@id="our-solutions-mobile"]/div[2]/a[4]/div[2]/svg')
            if third_search == "ok": #If our-solutions is found in the burger menu,
                third_click = driver.find_element("XPATH",'//*[@id="our-solutions-mobile"]/div[2]/a[4]/div[2]/svg')
                third_click.click() #click it
            else:
                sys.exit("broke at 3rd step, 3rd search")
        else:
            sys.exit("broke at 3rd step, 2nd search")
    elif current_search[0] == "retry": #if hamburger menu was not found,
        sub_search = condition_wait("ID", 'our-solutions-nav-link', "next") #check for the not expanded version of "our solutions" element
        if sub_search[0] == "ok":
            click_item = driver.find_element(By.ID,'our-solutions-nav-link')
            click_item.click() #if found, click on it 
            second_search = condition_wait("XPATH", '/html/body/nav/div[3]/div/div[1]/div[2]/a[4]/div[2]/svg')
            if second_search == "ok":
                second_click = driver.find_element(By.XPATH, '/html/body/nav/div[3]/div/div[1]/div[2]/a[4]/div[2]/svg')
                second_click.click()
            return
        elif sub_search[0] == "retry": #if not, look again...
            sub_search = condition_wait("ID", 'our-solutions-nav-link', "next")
            if sub_search[0] == "retry": #if the retry on the expanded 'our solutions' ID element fails...
                current_search = condition_wait("CLASS_NAME","hamburger-box") #do the original search for the hamburger menu again just incase it didn't load, and fail if not found
    elif current_search[0] == "fail":
        sys.exit("broke at 3rd step, 1st search")
    

    if len(third_search) > 2: #if the find element and retry fail:
        return_info = slice(1)
        return third_search[return_info] #should return "search_element" and "status_record" 
    else: #if passes:
        return third_search[1] #only returns search_element for testing purposes 

'''step 5'''
def step5(url = 'https://www.srsacquiom.com/solutions/m-a-dashboard/'):
    current_search = condition_wait("XPATH", '/html/body/main/div[3]/div/div/div[2]/a', "next") #search for "see the full suite"
    if current_search[0] == "retry":
        current_search = condition_wait("XPATH", '/html/body/main/div[3]/div/div/div[2]/a') #search again and will quit if retry fails
    elif current_search[0] == "fail":
        sys.exit("broke at 1st step")
        
    click_item = driver.find_element(By.XPATH, "XPATH", '/html/body/main/div[3]/div/div/div[2]/a')
    click_item.click()
    
    
    if len(current_search) > 2: #if the find element and retry fail:
        return_info = slice(1)
        return current_search[return_info] #should return "search_element" and "status_record" 
    else: #if passes:
        return current_search[1] #only returns search_element for testing purposes 
    
'''step 6'''
def step6(url = 'https://www.srsacquiom.com/solutions/'):
    current_search = condition_wait("XPATH", '/html/body/div[1]/div/div[1]/div[2]/a', 'next')
    if current_search[0] == "retry":
        current_search = condition_wait("XPATH", '/html/body/div[1]/div/div[1]/div[2]/a') #search again and will quit if retry fails
    elif current_search[0] == "fail":
        sys.exit("broke at 1st step")
    
    click_item = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/a')
    click_item.click()

    
    if len(current_search) > 2: #if the find element and retry fail:
        return_info = slice(1)
        return current_search[return_info] #should return "search_element" and "status_record" 
    else: #if passes:
        return current_search[1] #only returns search_element for testing purposes 

'''step 7'''
#return information 
def step7(url = 'https://www.srsacquiom.com/contact/'):
    phone_number = driver.find_element(By.XPATH ,'/html/body/main/div[1]/div[2]/div/div[1]/div/p[2]/a')
    op_hours = driver.find_element(By.XPATH, '/html/body/main/div[1]/div[2]/div/div[1]/div/p[3]')
    
    return [phone_number,  op_hours]

# ----------------------------------------- APPLICATION -----------------------------------------
step1()
step2()
step3_and_4()
step5()
step6()
step7()