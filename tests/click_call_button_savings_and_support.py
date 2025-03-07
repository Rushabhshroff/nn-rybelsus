import pytest
import time
from utils import accept_cookie,scroll_to_element
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_click_callbutton(selenium):
    selenium.get('https://rybelsus.com/savings-and-support.html')

    time.sleep(1)
    
    selenium.implicitly_wait(5)

    accept_cookie(selenium)

    call_button = selenium.find_element(By.CSS_SELECTOR,"[href=\"tel:%2518332752233\"]")

    scroll_to_element(selenium,call_button)

    call_button.click()
    
