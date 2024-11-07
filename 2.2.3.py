from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    s = int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)
    print(s)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(s))

    sub = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    sub.click()

finally:
    time.sleep(10)
    browser.quit()
