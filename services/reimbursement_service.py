from daos.reimbursement_dao import ReimbursementDao


class ReimbursementService:

    @staticmethod
    def create_reimbursement(reimbursement):
        return ReimbursementDao.create_reimbursement(reimbursement)

    @staticmethod
    def update_reimbursement(id, status_id, message):
        return ReimbursementDao.update_reimbursement(id, status_id, message)
