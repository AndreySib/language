import pytest
import time
link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_basket(browser):
    browser.get(link)
    time.sleep(30) 
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button, "Кнопка товар в корзину отсутсвует"
    
