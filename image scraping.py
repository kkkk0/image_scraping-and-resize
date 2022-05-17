from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

LINK = str(input('Input the full directory path to save images:'))
print('Previous directory:\t' + os.getcwd())
path = LINK
os.chdir(path)
print('Current directory:\t' + os.getcwd())

FILENAME = str(input('Input the abbreviation for your new images:'))

NUM = int(input("how many images do you want to download? "))
print(NUM)
KEYWORD = str(input("what do you want to search?"))
print(KEYWORD)

FORMAT = str(input("what is the image format do you want to download?"))

driver = webdriver.Chrome(r'C:\Users\HP\Desktop\Google Driver\chromedriver.exe')
driver.get("https://www.google.com/imghp?hl=eng")
driver.implicitly_wait(3)
elem = driver.find_element_by_name("q")
elem.send_keys(KEYWORD)
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

count = 1
for image in images:
    if count > NUM:
        break
    else:
        try:
            image.click()
            time.sleep(2)
            imgUrl = driver.find_element_by_xpath('/html/body/div[3]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute("src")
            if imgUrl.endswith('.' + FORMAT):
                opener=urllib.request.build_opener()
                opener.addheaders=[('User-Agent','Chrome/101.0.4951.64')]
                urllib.request.install_opener(opener)
                urllib.request.urlretrieve(imgUrl,FILENAME+ str(count) + ".jpg")
                print(count)
                count = count + 1
            else:
                continue
        except:
            pass

print('TQ. All done.')
time.sleep(2)
driver.close()




