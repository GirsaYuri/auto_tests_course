from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    def calc(x, y):
        return x + y

    x_element = browser.find_element(By.ID, "num1")
    x = int(x_element.text)
    y_element = browser.find_element(By.ID, "num2")
    y = int(y_element.text)

    answer = str(calc(x, y))
    print(answer)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(answer)
    button = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
    button.click()

    # inp = browser.find_element(By.ID, "answer")
    # inp.send_keys(y)
    # check_box = browser.find_element(By.ID, "robotCheckbox")
    # check_box.click()
    # radio = browser.find_element(By.ID, "robotsRule")
    # radio.click()
    # button = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
    # button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


