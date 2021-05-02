from controllers import course_controller, employee_controller, reimbursement_controller


def route(app):
    course_controller.route(app)
    employee_controller.route(app)
    reimbursement_controller.route(app)
