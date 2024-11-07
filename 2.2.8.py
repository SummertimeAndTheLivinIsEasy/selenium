from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import math
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    name.send_keys("name")

    surname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    surname.send_keys("surname")

    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("email")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'text_2_2_8.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.ID, "file") # находим элемент, который называется "выбрать файл"
    element.send_keys(file_path)

    sub = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    sub.click()


finally:
    time.sleep(10)
    browser.quit()
