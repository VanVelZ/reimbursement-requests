from daos.reimbursement_dao import ReimbursementDao


class ReimbursementService:

    @staticmethod
    def create_reimbursement(reimbursement):
        return ReimbursementDao.create_reimbursement(reimbursement)

    @staticmethod
    def update_reimbursement(id, status_id, message, amount):
        return ReimbursementDao.update_reimbursement(id, status_id, message, amount)

    @staticmethod
    def get_reimbursements_by_employee(id):
        reimbursements = ReimbursementDao.get_reimbursements_by_employee_id(id)
        serialized = []
        for reimbursement in reimbursements:
            serialized.append(reimbursement.serialize())
        return serialized