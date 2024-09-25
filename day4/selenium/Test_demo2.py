#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :Test_demo2.py
@说明        :
@时间        :2024/09/25 15:33:07
@作者        :chenyang
@版本        :1.0
'''


from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
# driver = webdriver.Chrome()
# driver = webdriver.Edge()
# driver.maximize_window()
driver.fullscreen_window()

username = "standard_user"
password = "secret_sauce"
login_url = "https://www.saucedemo.com/"
driver.get(login_url)

username_field = driver.find_element(By.ID, value="user-name")
password_field = driver.find_element(By.ID, value="password")


username_field.send_keys(username)
password_field.send_keys(password)

login_button = driver.find_element(By.ID, value="login-button")

login_button.click()

time.sleep(5)