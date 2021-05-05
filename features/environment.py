from selenium import webdriver
from selenium.webdriver.safari.webdriver import WebDriver


def before_all(context):
    driver: WebDriver = webdriver.Safari()

    context.driver = driver


def after_all(context):
    context.driver.quit()