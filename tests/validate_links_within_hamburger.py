import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import accept_cookie,scroll_to_element


def validate_link(selenium, link_element, expected_url):
    link_element.click()
    time.sleep(2)  
    assert selenium.current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {selenium.current_url}"
    time.sleep(2)  
    selenium.back()  
    

def test_validate_hamburger_links(selenium):
    selenium.get('https://rybelsus.com/')
    time.sleep(1)

    accept_cookie(selenium)

    hamburger_menu = selenium.find_element(By.CSS_SELECTOR, ".hamberger")
    hamburger_menu.click()
    time.sleep(1)

    # "Why RYBELSUS®" links
    why_rybelsus_dropdown = selenium.find_element(By.XPATH, "//a[@aria-label='More Why RYBELSUS®? pages']//span[@class='icon-chevron']")
    why_rybelsus_dropdown.click()
    time.sleep(1)

    link1 = selenium.find_element(By.XPATH, "(//a[contains(@class,'dropdown-link')])[1]")
    validate_link(selenium, link1, "https://www.rybelsus.com/why-rybelsus/rybelsus-results.html")

    link2 = selenium.find_element(By.XPATH, "(//a[contains(@class,'dropdown-link')])[2]")
    validate_link(selenium, link2, "https://www.rybelsus.com/why-rybelsus/rybelsus-vs-other-diabetes-pills.html")

    link3 = selenium.find_element(By.XPATH, "//a[contains(@href,'/why-rybelsus/how-rybelsus-works.html')]")
    validate_link(selenium, link3, "https://www.rybelsus.com/why-rybelsus/how-rybelsus-works.html")

    link4 = selenium.find_element(By.XPATH, "(//a[contains(@class,'dropdown-link')])[4]")
    validate_link(selenium, link4, "https://www.rybelsus.com/why-rybelsus/real-rybelsus-stories.html")

    # "Taking RYBELSUS®" links
    taking_rybelsus_dropdown = selenium.find_element(By.XPATH, "//a[contains(@aria-label,'More Taking RYBELSUS® pages')]//span[contains(@class,'icon-chevron')]")
    taking_rybelsus_dropdown.click()
    time.sleep(1)

    link5 = selenium.find_element(By.XPATH, "//a[contains(@href,'/taking-rybelsus/how-to-start-rybelsus.html')]")
    validate_link(selenium, link5, "https://www.rybelsus.com/taking-rybelsus/how-to-start-rybelsus.html")

    link6 = selenium.find_element(By.XPATH, "//a[contains(@href,'/taking-rybelsus/what-to-expect-with-rybelsus.html')]")
    validate_link(selenium, link6, "https://www.rybelsus.com/taking-rybelsus/what-to-expect-with-rybelsus.html")

    # "Savings & Support" link
    savings_support_link = selenium.find_element(By.XPATH, "//a[normalize-space()='Savings & Support']")
    validate_link(selenium, savings_support_link, "https://www.rybelsus.com/savings-and-support.html")

    # "FAQs" link
    faqs_link = selenium.find_element(By.XPATH, "//a[normalize-space()='FAQs']")
    validate_link(selenium, faqs_link, "https://www.rybelsus.com/faqs.html")

    selenium.execute_script("window.scrollBy(0, 500);")

    # "About Type 2 Diabetes" links
    about_diabetes_dropdown = selenium.find_element(By.XPATH, "//a[contains(@aria-label,'More About Type 2 Diabetes pages')]")
    about_diabetes_dropdown.click()
    time.sleep(1)

    link7 = selenium.find_element(By.XPATH, "//a[normalize-space()='What Is Type 2 Diabetes?']")
    validate_link(selenium, link7, "https://www.rybelsus.com/about-type-2-diabetes/what-is-type-2-diabetes.html")

    link8 = selenium.find_element(By.XPATH, "//a[normalize-space()='Type 2 Diabetes Lifestyle Tips']")
    validate_link(selenium, link8, "https://www.rybelsus.com/about-type-2-diabetes/type-2-diabetes-lifestyle-tips.html")

