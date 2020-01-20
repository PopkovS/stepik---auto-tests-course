from time import sleep

from selenium import webdriver

class ProgHubParser(object):
        def __init__(self, driver, lang):
            self.driver = driver
            self.lang = lang

        def parse(self):
            self.go_to_tests_page()

        def go_to_tests_page(self):
            self.driver.get("https://proghub.ru/tests")
            cart_elems = self.driver.find_elements_by_class_name("carousel__card")

            for elem in cart_elems:
                lang_link = elem.get_attribute('href')

                if self.lang in  lang_link:
                    language = lang_link.split("/")[-1]
                    self.driver.get()



def main ():
    driver = webdriver.Chrome()
    parser = ProgHubParser(driver, "python")
    parser.parse()
    # driver.get("https://proghub.ru/tests")
    # btn_elem = driver.find_element_by_css_selector(".home__meeting_banner_action_btn > span")
    # btn_elem.click()
    # title4 = driver.find_element_by_tag_name("h2")
    # print(title4.text)
    # sleep(5)

if __name__ == "__main__":
    main()