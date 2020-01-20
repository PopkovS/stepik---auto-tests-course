from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    # people_radio = browser.find_element_by_id("robotsRule")
    # people_checked = people_radio.get_attribute("checked")
    # print("value of people radio: ", people_checked)
    # assert people_checked == "true", "People radio is not selected by default"
    x = browser.find_element_by_id("treasure").get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector(".btn.btn-default").click()
    time.sleep(12)

    # welcome_text_elt = browser.find_element_by_tag_name("h1")
    #
    # welcome_text = welcome_text_elt.text
    #
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()