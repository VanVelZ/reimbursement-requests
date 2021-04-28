from models.reimbursement_status import ReimbursementStatus
from utils.db_connection import connection


class ReimbursementStatusDao:

    @staticmethod
    def get_all_status():
        sql = "Select * from reimbursement_status"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        status = []

        for record in records:
            status.append(ReimbursementStatus(id=record[0], name=record[1]))

        return status

    @staticmethod
    def get_status(id):
        sql = "Select * from reimbursement_status where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        record = cursor.fetchone()
        status = ReimbursementStatus(id=record[0], name=record[1])
        return status
