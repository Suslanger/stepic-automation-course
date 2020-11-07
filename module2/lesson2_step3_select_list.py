from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#num1").text
    y_element = browser.find_element_by_css_selector("#num2").text
    result = int(x_element) + int(y_element)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(result))
    button1 = browser.find_element_by_css_selector("button.btn.btn-default")
    button1.click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

