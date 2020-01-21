link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser1):
    browser1.get(link)
    browser1.find_element_by_css_selector("#login_link")