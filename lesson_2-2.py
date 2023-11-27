from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "img")
    x = x_element.get_attribute("valuex")
    print (x)
    y = calc(x)

    inp = browser.find_element(By.ID, "answer")
    inp.send_keys(y)
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


