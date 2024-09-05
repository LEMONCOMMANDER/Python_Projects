#from https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ
from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



#option + cmnd + c - copies the file path from the selected item in finder
# PATH = "/Users/lemonlord/Documents/Code_Stuff/Selenium_Web_Drivers/chromedriverr"
# driver = webdriver.Chrome(PATH)

# driver.get("https://www.techwithtim.net")

def test_args():
    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get('http://google.com')

    # time.sleep(100)
    time.sleep(5)
    text_area = driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')
    text_area.send_keys("big lebowski dude")
    time.sleep(1)
    text_area.send_keys(Keys.ENTER)
    # button = driver.find_element(by=By.XPATH, value = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
    # breakpoint()
    time.sleep(5)
    driver.quit()
    
    
test_args()