import pytest
import time
from utils import accept_cookie,scroll_to_element
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_click_getstarted(selenium):
    selenium.get('https://rybelsus.com/taking-rybelsus/how-to-start-rybelsus.html')

    time.sleep(1)

    accept_cookie(selenium)

    get_started_button = selenium.find_element(By.ID,"cta-af4c6e16ee-button")

    scroll_to_element(selenium,get_started_button)

    get_started_button.click()

    
    
