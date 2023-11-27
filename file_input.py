from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys('yuri')
    last_name = browser.find_element(By.NAME,"lastname")
    last_name.send_keys('girsa')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('girsau@mail.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(current_dir, "file.txt")
    input_file = browser.find_element(By.ID, 'file')
    input_file.send_keys(path)
    button = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
    button.click()


finally:
    time.sleep(20)
    browser.quit()