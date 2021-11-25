import pytest
import time
link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_basket(browser):
    browser.get(link)
    time.sleep(30) 
    
    assert browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button').is_displayed(), \
        'Кнопка товар в корзину отсутсвует'