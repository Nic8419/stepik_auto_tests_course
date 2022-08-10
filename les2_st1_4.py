import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("Nic")
    browser.find_element(By.NAME, 'lastname').send_keys('Sp')
    browser.find_element(By.NAME, "email").send_keys('xxx@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(10)
    browser.quit()