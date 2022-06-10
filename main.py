from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://aos/')

def main():

    buttonAddUser = '//*[@id="UserTableContainer_datagrid-row-r3-2-0"]/td[1]/div/a/span/span[2]'
    buttonUser = '//*[@id="menu"]/ul/li[2]/div[1]'
    buttonTools = '//*[@id="menu"]/ul/li[3]/div[3]'
    buttonToolsList = '//*[@id="menu"]/ul/li[3]/ul/li[2]/a'
    buttonThemeList = '//*[@id="menu"]/ul/li[4]/ul/li[2]/a'

    """Авторизация"""
    authorisation(login=login_password()[0], password=login_password()[1])

    # """ Переход на странице СТУ"""
    # click_button(buttonTools, buttonToolsList)

    """Переход на страницу Пользователи"""
    click_button(buttonUser, buttonUser)

    """Переход в карточку добаления пользователя"""
    click_button(buttonAddUser, buttonAddUser)

def click_button(findButton, clickButton):

    """Ожидаем прогрузки страницы и переход на вкладку"""
    try:
        element = WebDriverWait(driver, 10, 5).until(
            EC.visibility_of_element_located((By.XPATH, findButton))
        )
        element.click()
        driver.find_element(By.XPATH, clickButton).click()
    except:
        # driver.quit()
        print("Ошибка! Обьект не найден!",  findButton)





def authorisation(login, password):
    """Ввести логин, пароль и "Войти" """

    boxLogin = '//*[@id="loginField"]'
    boxPassword = '//*[@id="passwordField"]'
    buttonEnter = '//*[@id="formTab"]/div[3]/button'

    driver.find_element(By.XPATH, boxLogin).send_keys(login)
    driver.find_element(By.XPATH, boxPassword).send_keys(password)
    driver.find_element(By.XPATH, buttonEnter).click()


def login_password():
    login = 'Onil'
    password = '1'
    return login, password


# def create_user():
#     buttonUser = '//*[@id="menu"]/ul/li[2]'


main()