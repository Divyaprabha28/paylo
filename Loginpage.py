import driver as driver
from selenium import webdriver

class HomePageLocators(object):

  driver = webdriver.chrome(executable_path="/Users/divyaprabha/PycharmProjects/Paylocity/Drivers/chromedriver")



   username = driver.find_element_by_xpath("/html/body/div/main/div/div/form/div[2]/input")
   password = driver.find_element_by_xpath("/html/body/div/main/div/div/form/div[3]/input")


   driver.get("https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/LogIn")
