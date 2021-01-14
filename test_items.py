link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_verify_add_to_basket_button(browser):
    browser.get(link)
    assert len(browser.find_elements_by_css_selector(".btn-add-to-basket")) > 0, "'Add to cart' button is not present!"
