from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

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
    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
    button.click()

    # input1 = browser.find_element(By.TAG_NAME, "input")
    # input1.send_keys("Ivan")
    # x = browser.find_element(By.NAME, "last_name")
    # input2.send_keys("Petrov")
    # input3 = browser.find_element(By.CLASS_NAME, "city")
    # input3.send_keys("Smolensk")
    # input4 = browser.find_element(By.ID, "country")
    # input4.send_keys("Russia")
    # button = browser.find_element(By.XPATH, "//button[@type='submit']")
    # button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


