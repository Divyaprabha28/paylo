from selenium import webdriver
import pytest


def test_homepage():

    driver = webdriver.Chrome(executable_path='/Users/divyaprabha/PycharmProjects/Paylocity/Drivers/chromedriver')

    driver.get('https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/LogIn')

    driver.maximize_window()

    title = driver.title

    driver.close()