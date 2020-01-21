import os

import pyperclip as pyperclip
from selenium import webdriver
import time

def checkNum():
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_css_selector("[placeholder=\"Enter first name\"]")
    name.send_keys("Igor")
    firstName = browser.find_element_by_css_selector("[placeholder=\"Enter last name\"]")
    firstName.send_keys("Petrov")
    email = browser.find_element_by_css_selector("[placeholder=\"Enter email\"]")
    email.send_keys("testtest@test.com")
    # current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(os.getcwd(), 'dirt', 'testFile.txt')
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)
    browser.find_element_by_css_selector(".btn.btn-primary").click()
    checkNum()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()