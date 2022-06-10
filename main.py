from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://192.168.1.235/')

def main():



    buttonTools = '//*[@id="menu"]/ul/li[3]/div[1]'
    buttonToolsList = '//*[@id="menu"]/ul/li[3]/ul/li[2]/a'
    buttonThemeList = '//*[@id="menu"]/ul/li[4]/ul/li[2]/a'

    """Авторизация"""
    authorisation(login=login_password()[0], password=login_password()[1])


def click_button(findButton, clickOneButton, ClickTwoButton):
    """Ожидаем прогрузки страницы и переход на вкладку"""
    try:
        element = WebDriverWait(driver, 10, 2).until(
            EC.visibility_of_element_located((By.XPATH, findButton))
        )
        driver.find_element(By.XPATH, findButton).click()
        driver.find_element(By.XPATH, clickTwoButton).click()
    except:
        driver.quit()
        print("Обьект не найден!",  findButton)


def authorisation(login, password):
    """Ввести логин, пароль и "Войти" """

    boxLogin = '//*[@id="loginField"]'
    boxPassword = '//*[@id="passwordField"]'
    buttonEnter = '//*[@id="formTab"]/div[3]/button'
    driver.find_element(By.XPATH, boxLogin).send_keys(login)
    driver.find_element(By.XPATH, boxPassword).send_keys(password)
    driver.find_element(By.XPATH, buttonEnter).click()


def login_password():
    login = 'Otv_O_ShCh1_1'
    password = '123123Aa'
    return login, password


# def create_user():
#     buttonUser = '//*[@id="menu"]/ul/li[2]'


main()