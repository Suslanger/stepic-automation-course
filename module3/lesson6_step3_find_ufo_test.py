import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('path', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_find_ufo(browser, path):
    link = f"https://stepik.org/lesson/{path}/step/1"
    browser.get(link)
    input = browser.find_element_by_css_selector("textarea.textarea")
    answer = math.log(int(time.time()))
    input.send_keys(str(answer))

    btn = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
    )
    btn.click()
    result = browser.find_element_by_css_selector("pre.smart-hints__hint").text
    assert result == "Correct!"

