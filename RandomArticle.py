from selenium import webdriver
from selenium.webdriver.common.by import By
import random

y = input("base wiki search:")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

browser = webdriver.Chrome()

browser.get("https://en.wikipedia.org/wiki/" + y)

random.randint(1,4)


try:
    for i in range(4):
        print("attempt " + str(i))
            
            
        elem = browser.find_elements(By.PARTIAL_LINK_TEXT,"e")
        index = random.randint(0,len(elem)-1)
            
        element = elem[index]
        print()
        print(element.text)
        print(element.get_attribute('href'))
        if "en.wikipedia.org/wiki/" in element.get_attribute('href'):
            browser.execute_script("arguments[0].click();", element)
except:
    print(Exception)
    browser.close()
    exit()
    
x = input("Hit Enter to Exit, or Input any other key to continue ")
browser.close()