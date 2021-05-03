from flask import request

from services.employee_service import EmployeeService


def route(app):

    @app.route("/login/", methods=["GET"])
    def login():
        login_id = request.json["loginId"]
        return EmployeeService.login(login_id)
