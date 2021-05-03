from controllers import employee_controller, reimbursement_controller


def route(app):
    employee_controller.route(app)
    reimbursement_controller.route(app)
