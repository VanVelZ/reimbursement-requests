from selenium.webdriver.safari.webdriver import WebDriver


class ReimbursementPortal:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_textbox(self):
        return self.driver.find_element_by_id("loginId")

    def login_button(self):
        return self.driver.find_element_by_id("login")

    def logout_button(self):
        return self.driver.find_element_by_xpath('//*[@id="logout"]')

    def new_request_button(self):
        return self.driver.find_element_by_xpath('//*[@id="newRequest"]')

    def course_name(self):
        return self.driver.find_element_by_id("courseName")

    def course_type(self):
        return self.driver.find_element_by_id("courseType")

    def grading_format(self):
        return self.driver.find_element_by_id("gradingFormat")

    def start_date(self):
        return self.driver.find_element_by_id("start")

    def end_date(self):
        return self.driver.find_element_by_id("end")

    def course_cost(self):
        return self.driver.find_element_by_id("courseCost")

    def info(self):
        return self.driver.find_element_by_id("info")

    def submit(self):
        return self.driver.find_element_by_id("submit")

    def accept_buttons(self):
        return self.driver.find_elements_by_class_name("accept")

    def deny_buttons(self):
        return self.driver.find_elements_by_class_name("deny")

    def more_info_buttons(self):
        return self.driver.find_elements_by_class_name("moreinfo")
