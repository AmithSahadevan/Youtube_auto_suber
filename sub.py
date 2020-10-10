from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


email = input("enter your email: ")
passw = input("enter your password: ")

driver = webdriver.Chrome()
driver.get("https://stackoverflow.com/")

try:
    time.sleep(2)
    login = WebDriverWait(driver, 100).until(
        lambda driver: driver.find_element_by_xpath("/html/body/header/div/ol[2]/li[2]/a[1]")
    )
    login.click()

    time.sleep(5)

    login_with_google = WebDriverWait(driver, 100).until(
        lambda driver: driver.find_element_by_xpath("//*[@id='openid-buttons']/button[1]")
    )
    login_with_google.click()

    emailid = WebDriverWait(driver, 1000).until(
        lambda driver: driver.find_element_by_id("identifierId")
    )
    emailid.send_keys(email)
    time.sleep(2)
    emailid.send_keys(Keys.RETURN)

    password = WebDriverWait(driver, 100).until(
        lambda driver: driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
    )
    password.send_keys(passw)
    time.sleep(2)
    password.send_keys(Keys.RETURN)

    driver.get("https://www.youtube.com/channel/UC1sPrmI7GHPGkOYY5N_IyFg")

    time.sleep(2)

    sub = WebDriverWait(driver, 100).until(
        lambda driver: driver.find_element_by_id("subscribe-button")
    )
    sub.click()

    noti = WebDriverWait(driver, 100).until(
        lambda driver: driver.find_element_by_id("notification-preference-button")
    )
    noti.click()

    noti2 = WebDriverWait(driver, 100).until(
        lambda driver: driver.find_element_by_xpath("//*[@id='items']/ytd-menu-service-item-renderer[1]")
    )
    noti2.click()
    time.sleep(2)

finally:
    driver.quit()