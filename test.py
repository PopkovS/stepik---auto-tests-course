import unittest
from selenium import webdriver
import time

class TestReg(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_tag_name("input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder=\"Input your last name\"]")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("[placeholder=\"Input your email\"]")
        input3.send_keys("test@test.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be absolute value of a number")
        time.sleep(10)
        browser.quit()

if __name__ == "__main__":
    unittest.main()