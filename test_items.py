import time


def test_btn_add_to_basket_exists(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30)
    assert browser.find_element_by_css_selector('button.btn-add-to-basket'), 'add-to-basket button not found'
