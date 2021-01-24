from selenium import webdriver
import time
import unittest
import pytest


class TestRegistration(unittest.TestCase):
    def test_positive_register(self):
        link = "http://suninjuly.github.io/registration1.html"
        try:
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_css_selector(".first_block input.first")
            input1.send_keys("Vasya")
            input2 = browser.find_element_by_css_selector(".first_block input.second")
            input2.send_keys("Pupkin")
            input3 = browser.find_element_by_css_selector(".first_block input.third")
            input3.send_keys("vasya@pupkin.com")


            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            actual_result = welcome_text_elt.text
            expected_result = "Congratulations! You have successfully registered!"

            self.assertEqual(actual_result, expected_result, "text aren't equal")

        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()
             
    def test_negagtive_register(self):
        link = "http://suninjuly.github.io/registration2.html"
        try:
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_css_selector(".first_block input.first")
            input1.send_keys("Vasya")
            input2 = browser.find_element_by_css_selector(".first_block input.second")
            input2.send_keys("Pupkin")
            input3 = browser.find_element_by_css_selector(".first_block input.third")
            input3.send_keys("vasya@pupkin.com")


            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            actual_result = welcome_text_elt.text
            expected_result = "Congratulations! You have successfully registered!"

            self.assertEqual(actual_result, expected_result, "text aren't equal")

        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()

if __name__ == "__main__":
    unittest.main()
