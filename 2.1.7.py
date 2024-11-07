from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    y = calc(treasure)

    input_box = browser.find_element(By.ID, 'answer')
    input_box.send_keys(y)

    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()

    radio_btn = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    radio_btn.click()

    submit_btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_btn.click()

finally:
    time.sleep(10)
    browser.quit()
