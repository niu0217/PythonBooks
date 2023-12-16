from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://inventwithpython.com/')

# 点击页面
# linkElem = browser.find_element('link text', 'Automate the Boring Stuff with Python')
# linkElem.click()

# 模拟鼠标点击
htmlElem = browser.find_element('tag name', 'html')
htmlElem.send_keys(Keys.END)  # scrolls to bottom
