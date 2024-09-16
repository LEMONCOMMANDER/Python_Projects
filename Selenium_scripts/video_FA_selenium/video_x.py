from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# the following 2 imports allow us to introduce a wait period to ensure that a page has loaded and that the element could be found - we can also introduce timeouts
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#exception
from selenium.common.exceptions import TimeoutException


#video:
#https://www.youtube.com/watch?v=NB8OceGZGjA

'''
part 1 is about basic concepts of using selenium. The following is all notes and concepts to be used in your own testing. Part 2 will be a follow along example of testing against a 
game website called cookie clicker.



#the webdriver is an automation tool that lets us run automated testing calls through the browser
service = Service(executable_path="./chromedriver") #this works after manually opening the chromedriver file
# service = Service(executable_path="")
driver =webdriver.Chrome(service=service) #use docs to figure out what you can pass .Chrome - this may be through chromedriver docs instead of selenium

driver.get("https://google.com")

#WebDriverWait(driver, 5) #if after specified seconds nothing is found, exit
# more advanced is the following:
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "APjFqb"))
)# same wait and quit BUT if the specified element is found, continue instead
#we put this befoe the input_element to ensure the webpage loads. Then do the next steps if found


input_element =driver.find_element(By.ID, value="APjFqb") #can also be by=By.ID 
#taken from the find_element method:
# #def find_element(self, by=By.ID, value: Optional[str] = None) -> WebElement:

input_element.clear() #makes sure there is no existing text

#input_element =driver.find_element(By.ID, "APjFqb") - you can also just provide the value, but storing it as a variable seems to have better future usecase.
input_element.send_keys("big lebowski dude" + Keys.ENTER)



time.sleep(5)
driver.quit()
'''

'''
Part 2 | coockie clicker website -  https://orteil.dashnet.org/cookieclicker/
'''
status_count = 0

#sets selenium details
service = Service(executable_path=r'C:\Users\jibji\Documents\Code_Stuff\Python_Projects\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://orteil.dashnet.org/cookieclicker/')

#--------------------------------------------------------------------------------------------------------------------------------------------------------- HTML ID elements

cookie_id = "bigCookie"
cookies_id = "cookies"
upgrade_x_price = "productPrice" #for all upgrades, each one will have the same name but a number indicator - productPrice0 - well add this lter
upgrade_x_name = "product" #clicking on the div itself


#--------------------------------------------------------------------------------------------------------------------------------------------------------- HTML ID elements

#a function to add a wait and search for condition - the user can call this and pass the necessary information for any type of element
def condition_wait(search_type, value,  fail_command="exit"):
    global status_count
    print("ST: " + search_type)
    print("val: " + value)
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((getattr(By, search_type), value))
        )
        status = "found"
        print("found element: " + f"{value}")
        print("wait conditions run so far: " + str(status_count))
        status_count += 1
        return status #meant to leave this function and continue the code outside of the function
    except TimeoutException:
        print("didn't find element: " + f"{value}")
        print("wait conditions run so far: " + str(status_count))
        status_count += 1
        if fail_command == "next":
            status = "not found"
            print("user continue")
            return status #meant to leave this function and continue the code outside of the function
        else:
            print("user exit")
            #sys.exit() #needs to import sys at top
            SystemExit

#website asks for a language selection - lets see if it happens and then choose english. 
#runs the wait function which will wait 10 seconds and look for the language selector - if found, click english
current_status = condition_wait('XPATH', '//*[@id="langSelect-EN"]', 'next') 
#video uses XPATH here - while I decided to make the condition_wait a function, I followed along with XPATH method for practice
if current_status == "found":
    language = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
    language.click()
    
else:
    pass 

current_status = condition_wait("ID", "bigCookie", "next") #check to make sure element is there 

if current_status == "found":
    cookie = driver.find_element(By.ID, cookie_id) #errors if no variable=value syntax?
    cookie.click() #single click 
else:
    pass

while True: #from video, a click cycle
    cookie.click()
    #split the text string on spaces and take only the first element, which is the amount of cookies
    cookie_amount = driver.find_element(By.XPATH, '//*[@id="cookies"]').text.split(" ")[0] 
    cookie_amount = int(cookie_amount.replace(",","")) #removes all , by replacing it with nothing, turns it into an integer
    
    for i in range(4):
        upgrade_price = driver.find_element(By.ID, upgrade_x_price + str(i)).text.replace(",","")
        if not upgrade_price.isdigit():
            continue
        upgrade_price = int(upgrade_price)

        if cookie_amount >= upgrade_price:
            upgrade = driver.find_element(By.ID, upgrade_x_name + str(i))
            upgrade.click()
            break