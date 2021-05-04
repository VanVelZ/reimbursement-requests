from flask import request

from models.reimbursement import Reimbursement
from services.reimbursement_service import ReimbursementService


def route(app):

    @app.route("/reimbursement/", methods=["PUT"])
    def create_reimbursement():
        reimbursement = Reimbursement.deserialize(request.json)
        did_submit = ReimbursementService.create_reimbursement(reimbursement)
        if did_submit:
            return "Great!", 200
        else:
            return "NOOOO", 400

    @app.route("/reimbursement/<id>", methods=["PATCH"])
    def update_reimbursement(id):
        status_id = request.json["statusId"]
        message = request.json["message"]
        return ReimbursementService.update_reimbursement(id, status_id , message)