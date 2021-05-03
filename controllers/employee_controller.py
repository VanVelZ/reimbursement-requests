from flask import request, jsonify, session

from services.employee_service import EmployeeService


def route(app):

    @app.route("/employees/", methods=["POST"])
    def login():
        login_id = request.json["loginId"]
        return jsonify(EmployeeService.login(login_id).serialize())
