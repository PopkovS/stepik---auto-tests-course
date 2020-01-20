import math
import os

import pyperclip as pyperclip
from selenium import webdriver
import time

def checkNum():
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector(".trollface.btn.btn-primary").click()
    print(browser.window_handles)
    browser.switch_to_window(browser.window_handles[1])

    x = browser.find_element_by_id("input_value").text
    print(x)
    x = calc(x)
    # print(x)
    browser.find_element_by_id("answer").send_keys(x)
    browser.find_element_by_css_selector(".btn.btn-primary").click()
    checkNum()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()