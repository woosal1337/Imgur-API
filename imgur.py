import os
import time
import imgurpython
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def authenticate():
    f = open("user.token", "r")
    client_id, client_secret, userName, Password = f.readline().split(";")
    f.close()

    client = imgurpython.ImgurClient(client_id, client_secret)
    authorization_url = client.get_auth_url("pin")
    print(authorization_url)

    driver = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
    driver.get(authorization_url)

    imgUsername = driver.find_element_by_xpath('//*[@id="username"]')
    imgPassword = driver.find_element_by_xpath('//*[@id="password"]')
    imgUsername.send_keys(userName)
    imgPassword.send_keys(Password)

    driver.find_element_by_name("allow").click()

    timeout = 3

    try:
        element_present = EC.presence_of_element_located((By.ID, "pin"))
        WebDriverWait(driver, timeout).until(element_present)
        pin_element = driver.find_element_by_id("pin")
        pin = pin_element.get_attribute("value")
    except TimeoutException:
        print("Could not load within the time")
    driver.close()

    credentials = client.authorize(pin, "pin")
    client.set_user_auth(credentials["access_token"], credentials)
    print("AUTH SUCCESSFULL")

    return client


if __name__ == "__main__":
    authenticate()