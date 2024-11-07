from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.CLASS_NAME, "trollface")
    btn.click()
    # browser.find_element_by_css_selector('button.trollface').click()

    new_window = browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    input_box = browser.find_element(By.ID, "answer")
    input_box.send_keys(y)

    btn2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn2.click()


finally:
    time.sleep(10)
    browser.quit()