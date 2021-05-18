import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_chek_button(browser):
    try:
        browser.get(link)
        time.sleep(30)
        browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
        k=1
    except NoSuchElementException:
        k=0
    finally:
        assert k==1, "Кнопка не найдена"


