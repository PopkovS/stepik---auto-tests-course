import time
import math
import pytest
from selenium import webdriver

# answer = str(math.log(int(time.time())))
# print(answer)

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    

class TestMainPage1():
    @pytest.mark.parametrize('links', ["895", "896", "897", "898", "899", "903", "904", "905"])
    def test_guest_should_see_login_link(self, browser, links):
        browser.implicitly_wait(15)
        answer = str(math.log(int(time.time())))
        link = f"https://stepik.org/lesson/236{links}/step/1"
        browser.get(link)
        text_area = browser.find_element_by_css_selector(".textarea.string-quiz__textarea.ember-text-area.ember-view")
        text_area.send_keys(answer)
        submit = browser.find_element_by_css_selector(".submit-submission")
        submit.click()
        result = browser.find_element_by_css_selector(".smart-hints__hint").text
        print(f"\nРезультат с сайта {link} следующий:\n{result}")
        assert result == "Correct!", "\nЗдесь что то не так"
        

