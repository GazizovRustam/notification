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

    autorisation(login, password, boxLogin, boxPassword)



def autorisation(login, password, lineAddressLogin, lineAddressPassword):

    # """Найти поле ввода логин и пароль"""
    # inputBoxLogin = seearchBox(lineAddressLogin)
    # inputBoxPassword = seearchBox(lineAddressPassword)

    """Ввести логин и пароль"""
    sendKeys(seearchBox(lineAddressLogin), login)
    sendKeys(seearchBox(lineAddressPassword), password)


    # """Нажать кнопку "Войти"""""
    # clickEnter = seearchBox()
    #
    #
    #
    #
    # seearchButton = driver.find_element(By.XPATH, buttonEnter)
    # seearchButton.click()



def seearchBox(path):
    box = driver.find_element(By.XPATH, path)
    return box


def sendKeys(box, value):
    box.send_keys(value)


def clickButton(button):
    button.click()




    # seearchBoxPassword = driver.find_element(By.XPATH, boxPassword)
    # seearchBoxPassword.send_keys(password)
    # seearchButton = driver.find_element(By.XPATH, '//*[@id="formTab"]/div[3]/button')
    # seearchButton.click()



# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '/html/body/header/nav/ul/li[3]/div[2]')))
# finally:
#     seearchButtonStu = driver.find_element(By.XPATH, buttonTools)
#     seearchButtonStu.click()
#     searchButtonStuP = driver.find_element(By.XPATH, buttonToolsList)
#     searchButtonStuP.click()
#     time.sleep(3)
#     driver.quit()
main()