from utils import accept_cookie,scroll_to_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_click_getstarted(selenium):
    missing_anchors=[]
    selenium.get('https://rybelsus.com/faqs.html')
    WebDriverWait(selenium,5).until(EC.presence_of_element_located((By.ID,'onetrust-accept-btn-handler')))
    accept_cookie(selenium)
    elements=selenium.find_elements(By.XPATH,'//div[@class="accordion"]/div')
    for ele in elements:
        scroll_to_element(selenium,ele)
        ele.click()
        try:
            anchor = WebDriverWait(ele, 5).until(
                EC.presence_of_element_located((By.XPATH, './/a')))
            href_text=anchor.get_attribute('href')
            if not href_text.strip():
                missing_anchors.append(ele)
        except Exception as e:
            missing_anchors.append(ele)  
    assert not missing_anchors, f"{len(missing_anchors)} anchors are missing 'href' attribute!"