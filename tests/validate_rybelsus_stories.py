import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utils import accept_cookie,scroll_to_element


def validate_element(selenium, xpath, expected_text):
    element = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    assert expected_text in element.text, f"Expected text: {expected_text}, Actual text: {element.text}"
    print(f"Validated element with text: {expected_text}")

def test_validate_rybelsus_stories(selenium):
    selenium.get('https://rybelsus.com/why-rybelsus/real-rybelsus-stories.html')
    time.sleep(5)

    accept_cookie(selenium)

    first_story = selenium.find_element(By.XPATH,"//p[contains(text(),'Beto is a family man and a mechanic who was down t')]")
    scroll_to_element(selenium,first_story)
    validate_element(selenium, "//p[contains(text(),'Beto is a family man and a mechanic who was down t')]", "Beto is a family man and a mechanic who was down t")

    second_story = selenium.find_element(By.XPATH,"//strong[contains(text(),'After starting on 3 mg for 30 days and moving to 7')]")
    scroll_to_element(selenium,second_story)
    validate_element(selenium, "//strong[contains(text(),'After starting on 3 mg for 30 days and moving to 7')]", "After starting on 3 mg for 30 days and moving to 7")

    Troy_image = selenium.find_element(By.XPATH, "//img[@alt='Troy']")
    scroll_to_element(selenium, Troy_image)
    Troy_image.click()
    time.sleep(2)
    third_story = selenium.find_element(By.XPATH,"//span[contains(text(),'Troy is a loving husband and pet owner who enjoys ')]")
    scroll_to_element(selenium,third_story)
    validate_element(selenium, "//span[contains(text(),'Troy is a loving husband and pet owner who enjoys ')]", "Troy is a loving husband and pet owner who enjoys ")


    carolyn_image = selenium.find_element(By.XPATH, "//img[@alt='Carolyn']")
    scroll_to_element(selenium, carolyn_image)
    carolyn_image.click()
    time.sleep(2)
    fourth_story = selenium.find_element(By.XPATH,"//span[contains(text(),'Carolyn shows her true colors as a painter and som')]")
    scroll_to_element(selenium,fourth_story)
    validate_element(selenium, "//span[contains(text(),'Carolyn shows her true colors as a painter and som')]", "Carolyn shows her true colors as a painter and som")


    beto_image = selenium.find_element(By.XPATH, "//img[@alt='Beto']")
    scroll_to_element(selenium, beto_image)
    beto_image.click()
    time.sleep(2)
    fifth_story = selenium.find_element(By.XPATH,"//span[contains(text(),'Beto is a family man and a mechanic who was down t')]")
    scroll_to_element(selenium,fifth_story)
    validate_element(selenium, "//span[contains(text(),'Beto is a family man and a mechanic who was down t')]", "Beto is a family man and a mechanic who was down t")