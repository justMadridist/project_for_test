from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can__goto_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # init page check
    page.open()                      # page opening
    page.should_be_login_link()         # looking for login link

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # init page check
    page.open()                      # page opening
    page.go_to_login_page()          # going to login page
