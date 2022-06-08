from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://192.168.1.235/')

def main():
    login = 'Otv_O_ShCh1_1'
    password = '123123Aa'
    boxLogin = '//*[@id="loginField"]'
    boxPassword = '//*[@id="passwordField"]'
    buttonEnter = '//*[@id="formTab"]/div[3]/button'
    buttonTools = '//*[@id="menu"]/ul/li[3]/div[1]'
    buttonToolsList = '//*[@id="menu"]/ul/li[3]/ul/li[2]/a'

    """Авторизация"""
    authorisation(login, password, boxLogin, boxPassword, buttonEnter)

    """Ожидаем прогрузки страницы и переход на вкладку Средства ТУ"""
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/header/nav/ul/li[3]/div[2]')))
    finally:
        clickButton(seearchBox(buttonTools))
        clickButton(seearchBox(buttonToolsList))
        time.sleep(5)
        driver.quit()


def authorisation(login, password, lineAddressLogin, lineAddressPassword, lineAddressEnter):
    """Ввести логин, пароль и "Войти" """
    sendKeys(seearchBox(lineAddressLogin), login)
    sendKeys(seearchBox(lineAddressPassword), password)
    clickButton(seearchBox(lineAddressEnter))


def seearchBox(path):
    box = driver.find_element(By.XPATH, path)
    return box


def sendKeys(box, value):
    box.send_keys(value)


def clickButton(button):
    button.click()


main()