from models.reimbursement_status import ReimbursementStatus
from utils.db_connection import connection


class ReimbursementStatusDao:

    @staticmethod
    def get_all_statuss():
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

    @staticmethod
    def update_status(changing_status):
        sql = "Update reimbursement_status set name=%s where id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [changing_status.name, changing_status.id])
        connection.commit()
        return changing_status

    @staticmethod
    def delete_status(id):
        sql = "Delete from reimbursement_status where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        connection.commit()
        return cursor.rowcount

    @staticmethod
    def create_status(status):
        sql = "Insert into reimbursement_status values (default, %s)"
        cursor = connection.cursor()
        cursor.execute(sql, [status.name])
        connection.commit()
        return True
