
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get('https://www.citilink.ru/')

def main():

    buttonDelivery = '/html/body/div[2]/div[2]/header/div[1]/div[2]/div[3]/div/div/div[1]/a[4]'
    buttonCatalog = '/html/body/div[2]/div[1]/header/div[2]/div[1]/div[2]/a/button'
    buttonTools = '//*[@id="overlay"]/ul/li[2]/a'
    buttonPhone = '//*[@id="features"]/div/div/div[4]/a'
    buttonThemeList = ''
    boxFind = '/html/body/div[2]/div[2]/header/div[2]/div[2]/div[1]/div/div/form/div/div[1]/div/label/input'
    box = 'Кондиционеры'
    """Авторизация"""
    #authorisation(login=login_password()[0], password=login_password()[1])

    """ Переход на странице ситилинк"""
    #click_button(buttonDelivery)
    click_button(boxFind, box)
    click_buttton()



    # """Переход на страницу Пользователи"""
    # click_button(buttonUser, buttonUser)

    # """Переход в карточку добаления пользователя"""
    # click_button(buttonAddUser, buttonAddUser)
def click_button(findButton, keys=""):

    """Ожидаем прогрузки страницы и переход на вкладку"""
    try:

        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, findButton).click()
        driver.find_element(By.XPATH, findButton).send_keys(keys)



    except:
        # driver.quit()
        print("Ошибка! Обьект не найден!",  findButton)





def authorisation(login, password):
    """Ввести логин, пароль и "Войти" """

    boxLogin = '/html/body/app-root/div/div/div[2]/main/app-login-finnair-plus/div/div[2]/form/div[1]/label/div/input'
    boxPassword = '/html/body/app-root/div/div/div[2]/main/app-login-finnair-plus/div/div[2]/form/div[2]/label/div/input'
    buttonEnter = '/html/body/app-root/div/div/div[2]/main/app-login-finnair-plus/div/div[2]/form/button'
    buttonLogin = '/html/body/fin-app/div/fin-set-language/span/fin-layout/fin-header/header/div[1]/div[2]/div[2]/fin-login-button/button/span/span'

    click_button(buttonLogin)
    driver.find_element(By.XPATH, boxLogin).send_keys(login)
    driver.find_element(By.XPATH, boxPassword).send_keys(password)
    driver.find_element(By.XPATH, buttonEnter).click()


def login_password():
    login = 'karl.karl10@mail.ru'
    password = '123123Aa'
    return login, password



main()