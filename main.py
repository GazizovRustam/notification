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

    buttonTools = '//*[@id="menu"]/ul/li[3]/div[1]'
    buttonToolsList = '//*[@id="menu"]/ul/li[3]/ul/li[2]/a'

    """Авторизация"""
    authorisation(login, password)

    """Ожидаем прогрузки страницы и переход на вкладку Средства ТУ"""
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/header/nav/ul/li[3]/div[2]')))
    finally:
        driver.find_element(By.XPATH, buttonTools).click()
        driver.find_element(By.XPATH, buttonToolsList).click()
        time.sleep(5)
        driver.quit()


def authorisation(login, password):
    """Ввести логин, пароль и "Войти" """

    boxLogin = '//*[@id="loginField"]'
    boxPassword = '//*[@id="passwordField"]'
    buttonEnter = '//*[@id="formTab"]/div[3]/button'
    driver.find_element(By.XPATH, boxLogin).send_keys(login)
    driver.find_element(By.XPATH, boxPassword).send_keys(password)
    driver.find_element(By.XPATH, buttonEnter).click()


main()