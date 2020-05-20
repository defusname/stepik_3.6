def test_works_button_add_to_basket(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = len(browser.find_elements_by_css_selector('button.btn-add-to-basket'))
    assert button > 0, 'Button is not found!'
