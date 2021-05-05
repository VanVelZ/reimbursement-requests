from selenium import webdriver
from selenium.webdriver.safari.webdriver import WebDriver

from features.pages.reimbursement_portal import ReimbursementPortal


def before_all(context):
    driver: WebDriver = webdriver.Safari()
    driver.maximize_window()
    reimbursement_portal = ReimbursementPortal(driver)

    context.driver = driver
    context.reimbursement_portal = reimbursement_portal


def after_all(context):
    context.driver.quit()