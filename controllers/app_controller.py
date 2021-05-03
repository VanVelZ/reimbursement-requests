from controllers import employee_controller, reimbursement_controller
from flask_cors import CORS


def route(app):
    employee_controller.route(app)
    reimbursement_controller.route(app)
    CORS(app)
