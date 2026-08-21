import os

import dotenv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

dotenv.load_dotenv()
site_url = os.getenv("SITE")
opt1 = os.getenv("OPT1")

if not site_url:
    site_url = input("what site are we testing?")

if opt1 and opt1 == "login":
    username = os.getenv("UNAME")
    password = os.getenv("PASSW")

    driver.get(f"{site_url}")
    opt2 = os.getenv("OPT2")
    if not opt2:
        opt2 = input("what is the id of the login section?")

    driver.implicitly_wait(10)
    login_element = driver.find_element(By.ID, f"{opt2}")
    # login_element = driver.find_element(By.CLASS_NAME, f"{opt2}")
    # print(login_element.get_attribute("outerHTML"))

    if not username:
        username = input("enter username")
    if not password:
        password = input("enter password")

    driver.implicitly_wait(10)
    login_element.find_element(By.NAME, "username").send_keys(username)

    login_element.find_element(By.NAME, "password").send_keys(password)
    login_element.find_element(By.NAME, "login").click()
    driver.implicitly_wait(10)

    home_page = driver.find_element(By.TAG_NAME, "body")
    # print(home_page.get_attribute("innerHTML"))




done = False
while not done:
    done_eval = input("type 'yes' when you are done using this browser: ")
    if done_eval == "yes" or done_eval == 1 or done_eval == "y":
        done = True

driver.quit()
