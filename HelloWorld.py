from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Chromedriver initialisation
driver = webdriver.Chrome('D:\Selenium Practices\chromedriver-win64\chromedriver.exe')

#task 1: Basic Browser Automation
url = "https://www.wikipedia.org/"
driver.get(url)
driver.maximize_window()
print(driver.title)

#task 2: Element Locating and interaction
searchBar = driver.find_element(By.XPATH, "//*[@id='searchInput']")
searchBar.send_keys("Selenium (software)")
# searchBar.send_keys(Keys.RETURN) -- for enter key action
searchButton = driver.find_element(By.XPATH, "//button[@type='submit']")
searchButton.click() # for click action

#task 3: Take screenshot and print confirmation
image = driver.save_screenshot("wikipedia_selenium_search.png")
if(image):
    print("Screenshot taken successfully")
else:
    print("Unable to take screenshot")
    
time.sleep(5) #display the screen for 5 seconds
driver.quit() #ends the program