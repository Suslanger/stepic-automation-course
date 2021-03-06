from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button1 = browser.find_element_by_css_selector("#book")
button1.click()
x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_css_selector("#answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
input1.send_keys(y)
button2 = browser.find_element_by_css_selector("#solve")
button2.click()


# успеваем скопировать код за 5 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()
