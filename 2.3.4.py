from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    # button = browser.find_element_by_class_name('btn-primary').click()
    btn.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    input_box = browser.find_element(By.ID, "answer")
    input_box.send_keys(y)

    btn2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn2.click()

finally:
    time.sleep(10)
    browser.quit()