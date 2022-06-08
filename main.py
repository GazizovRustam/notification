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
    buttonTools = '//*[@id="menu"]/ul/li[3]/div[1]'
    buttonToolsList = '//*[@id="menu"]/ul/li[3]/ul/li[2]/a'

    """Найти поле ввода логин и ввести"""
    login_box = seearchBox(boxLogin)
    sendKeys(login_box, login)
    """Найти поле ввода пароль и ввести"""
    find_password_box = seearchBox(boxPassword)
    sendKeys(find_password_box, password)


#def autorisation(login, password):


def seearchBox(path):
    box = driver.find_element(By.XPATH, path)
    return box


def sendKeys(box, login):
    box.send_keys(login)




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
#     #time.sleep(10)
#     #driver.quit()
main()