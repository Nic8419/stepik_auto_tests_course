from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    browser.find_element(By.TAG_NAME, 'button').click()

    num_is = browser.find_element(By.ID, 'input_value').text
    new_num = str(math.log(abs(12*math.sin(int(num_is)))))

    browser.find_element(By.ID,'answer').send_keys(new_num)
    browser.find_element(By.ID,'solve').click()

finally:
    browser.quit()
