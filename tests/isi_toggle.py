import pytest
import time 
from utils import accept_cookie,javascript_click
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_isi_toggle(selenium):
    selenium.get('https://rybelsus.com/why-rybelsus/real-rybelsus-stories.html')

    time.sleep(1)

    accept_cookie(selenium)

    javascript_click(selenium,selenium.find_element(By.ID,"isi-toggle"))

    time.sleep(1)

    javascript_click(selenium,selenium.find_element(By.ID,"isi-toggle"))




    