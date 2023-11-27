from selenium import webdriver
from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.ui import Select
# import math
import os
#
link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)


    inp = browser.find_element(By.ID, "answer")
    inp.send_keys(y)
    browser.execute_script("window.scrollBy(0, 150);")
    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

#
# print(os.path.abspath(__file__))
#
# print(os.path.abspath(os.path.dirname(__file__)))