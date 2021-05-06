from models.reimbursement_status import ReimbursementStatus
from utils.db_connection import connection


class ReimbursementStatusDao:

    @staticmethod
    def get_status(id):
        sql = "Select * from reimbursement_status where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        record = cursor.fetchone()
        status = ReimbursementStatus(id=record[0], name=record[1])
        return status
