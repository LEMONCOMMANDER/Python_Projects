from selenium import webdriver

#option + cmnd + c - copies the file path from the selected item in finder
#oPATH = "/Users/lemonlord/Documents/Code_Stuff/Selenium_Web_Drivers/chromedriver"
driver = webdriver.Chrome()

driver.get("https://www.techwithtim.net")
print(driver.title)
driver.quit()
