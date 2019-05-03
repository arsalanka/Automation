from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import time

#Typein UserName and Password
usernameStr = 'USERNAME'
passwordStr = 'Password'
#Check Location of Chromedriver
browser = webdriver.Chrome(executable_path='C:\Python\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')
browser.get(('https://facbook.com/login.php'))
# fill in username and hit the next button
username = browser.find_element_by_id('email')
username.send_keys(usernameStr)

# wait for transition then continue to fill items
password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'pass')))
password.send_keys(passwordStr)
 
signInButton = browser.find_element_by_id('loginbutton')
signInButton.click()
profile = browser.find_element_by_xpath("//*[@class='_2s25 _606w']")
logoSRC = profile.get_attribute("href");
browser.get((logoSRC))
print(logoSRC)

profile = browser.find_element_by_xpath("//*[@class='_1nv3 _11kg _1nv5 profilePicThumb']")
logoSRC = profile.get_attribute("href");
browser.get((logoSRC))

profile = browser.find_element_by_xpath("//*[@class='_s0 _4ooo _1x2_ _1ve7 _4nos img']") 
logoSRC = profile.get_attribute("src");
print(logoSRC)

urllib.request.urlretrieve(logoSRC, "profilePic.png")

browser.quit()
exit()






