from time import sleep

from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.safari.webdriver import WebDriver


@given(u'The User is on the log in page')
def on_login_page(context):
    driver: WebDriver = context.driver
    driver.get("file:///Users/prozachrx/Documents/Revature/reimbursements/presentation/login.html")


@when(u'The User enters a correct Id')
def user_enter_id(context):
    context.reimbursement_portal.login_textbox().send_keys("100006")
    sleep(2)


@when(u'The User Clicks submit')
def user_click_submit(context):
    context.reimbursement_portal.login_button().click()
    sleep(3)


@then(u'The User will be on the home page')
def user_on_home(context):
    assert context.driver.title == "Reimbursement Home"

@when(u'The supervisor enters a correct Id')
def supervisor_enter_id(context):
    context.reimbursement_portal.login_textbox().send_keys("100000")


@when(u'The Department Head enters a correct Id')
def department_head_enter_id(context):
    context.reimbursement_portal.login_textbox().send_keys("100001")


@when(u'The Benefits Coordinator enters a correct Id')
def benco_enter_id(context):
    context.reimbursement_portal.login_textbox().send_keys("100003")


@given(u'The User is logged in')
def user_logged_in(context):
    on_login_page(context)
    context.reimbursement_portal.login_textbox().send_keys("200004")
    context.reimbursement_portal.login_button().click()
    sleep(2)


@given(u'The User is on the home page')
def user_on_home_page(context):
    assert context.driver.title == "Reimbursement Home"


@when(u'The User clicks on Start New')
def user_starts_request(context):
    context.reimbursement_portal.new_request_button().click()
    sleep(2)


@when(u'The User Enters All of the required info')
def user_enters_info(context):
    page = context.reimbursement_portal
    page.course_name().send_keys("How to ball chase in Rocket League")
    page.start_date().send_keys("06" + Keys.TAB + "15" + Keys.TAB + "2021")
    page.start_date().send_keys("06" + Keys.TAB + "15" + Keys.TAB + "2021")
    page.course_cost().send_keys("100")
    page.info().send_keys("It is really important and relevant to my work")
    page.submit().click()
    sleep(3)


@then(u'The User is Redirected to the home page')
def user_on_home(context):
    assert context.driver.title == "Reimbursement Home"


@given(u'The Supervisor is logged in')
def supervisor_logged_in(context):
    on_login_page(context)
    context.reimbursement_portal.login_textbox().send_keys("100000")
    context.reimbursement_portal.login_button().click()
    sleep(2)


@given(u'A request is pending')
def request_pending(context):
    assert context.reimbursement_portal.accept_buttons()


@when(u'The User clicks the Accept button')
def clicks_accept(context):
    buttons = context.reimbursement_portal.accept_buttons()
    context.request_count = len(buttons)
    buttons[0].click()
    sleep(2)


@then(u'The request is approved by the user')
def request_approved(context):
    print(len(context.reimbursement_portal.accept_buttons()), context.request_count)
    assert len(context.reimbursement_portal.accept_buttons()) < context.request_count


@given(u'The Department Head is logged in')
def department_head_logged_in(context):
    on_login_page(context)
    context.reimbursement_portal.login_textbox().send_keys("100002")
    context.reimbursement_portal.login_button().click()
    sleep(2)


@given(u'The Benefits Coordinator is logged in')
def benco_logged_in(context):
    on_login_page(context)
    context.reimbursement_portal.login_textbox().send_keys("100003")
    context.reimbursement_portal.login_button().click()
    sleep(2)


@when(u'The User clicks the Deny button')
def clicks_deny(context):
    buttons = context.reimbursement_portal.deny_buttons()
    context.request_count = len(buttons)
    buttons[0].click()
    sleep(2)


@then(u'The request is denied by the user')
def is_denied(context):
    print(len(context.reimbursement_portal.accept_buttons()), context.request_count)
    assert len(context.reimbursement_portal.accept_buttons()) < context.request_count


@when(u'The User clicks the request more info button')
def request_more_info(context):
    buttons = context.reimbursement_portal.deny_buttons()
    context.request_count = len(buttons)
    buttons[0].click()
    sleep(2)


@then(u'The request is forwarded to the user')
def forwarded_to_requester(context):
    print(len(context.reimbursement_portal.accept_buttons()), context.request_count)
    assert len(context.reimbursement_portal.accept_buttons()) < context.request_count
