from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("input[name='firstname']")
    input1.send_keys("Aba-ba")
    input2 = browser.find_element_by_css_selector("input[name='lastname']")
    input2.send_keys("Ga-la-ma-ga")
    input3 = browser.find_element_by_css_selector("input[name='email']")
    input3.send_keys("Ababa@galamaga.com")
    element = browser.find_element_by_css_selector("input[name='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'text.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)

    button1 = browser.find_element_by_css_selector("button.btn.btn-primary")
    button1.click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
