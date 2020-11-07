from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    checkbox1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox1.click()
    radio1 = browser.find_element_by_css_selector("[for='robotsRule']")
    radio1.click()
    button1 = browser.find_element_by_css_selector("button.btn.btn-default")
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

