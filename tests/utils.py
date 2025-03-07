import pytest
import requests
import os
import base64
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

def accept_cookie(selenium):
    acceptButton = selenium.find_element(By.ID,"onetrust-accept-btn-handler")
    acceptButton.click()

def scroll_to_element(selenium,element):
    selenium.execute_script("arguments[0].scrollIntoView();", element)

def javascript_click(selenium,element):
    selenium.execute_script("arguments[0].click();", element)

def click_by_coordinates(selenium,element):
    actions = ActionChains(selenium)
    actions.move_to_element(element)
    actions.click().perform()

def get_contexts(selenium):
    session_id = selenium.session_id
    appium_url = f'http://hub.browserstack.com/wd/hub/session/{session_id}/contexts'

    username = os.getenv('BROWSERSTACK_USERNAME')
    access_key = os.getenv('BROWSERSTACK_ACCESS_KEY')
    credentials = f"{username}:{access_key}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode('utf-8')
    headers = {
        'Authorization': f'Basic {encoded_credentials}',
    }
    response = requests.get(appium_url,headers=headers)
    if response.status_code == 200:
        contexts = response.json().get('value', [])
        print(f"Available contexts: {contexts}")
        return contexts
    else:
        print(f"Failed to get contexts. Status code: {response.status_code}")
        print("Response:", response.text)
        return []


def switch_context(selenium, context):
    session_id = selenium.session_id
    appium_url = f'http://hub.browserstack.com/wd/hub/session/{session_id}/context'
    payload = {
        "name": context,
        'Authorization': ''
    }
    username = os.getenv('BROWSERSTACK_USERNAME')
    access_key = os.getenv('BROWSERSTACK_ACCESS_KEY')
    credentials = f"{username}:{access_key}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode('utf-8')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {encoded_credentials}',
    }
    response = requests.post(appium_url, json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Context switched to '{context}' successfully.")
    else:
        print(f"Failed to switch context. Status code: {response.status_code}")
        print("Response:", response.text)
