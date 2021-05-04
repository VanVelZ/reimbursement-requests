from daos.course_dao import CourseDao
from daos.employee_dao import EmployeeDao
from daos.reimbursement_status_dao import ReimbursementStatusDao
from models.reimbursement import Reimbursement
from utils.db_connection import connection


class ReimbursementDao:

    @staticmethod
    def get_all_reimbursements():
        sql = "Select * from reimbursements"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        reimbursements = []

        for record in records:
            reimbursement = Reimbursement(id=record[0], date_submitted=record[3], amount=record[5], message=record[6])
            reimbursement.course = CourseDao.get_course(record[4])
            reimbursement.employee = EmployeeDao.get_employee(record[1])
            reimbursement.status = ReimbursementStatusDao.get_status(record[2])
            reimbursements.append(reimbursement)

        return reimbursements

    @staticmethod
    def get_reimbursement(id):
        sql = "Select * from reimbursement_types where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        record = cursor.fetchone()
        reimbursement = Reimbursement(id=record[0], date_submitted=record[3], amount=record[5], message=record[6])
        reimbursement.course = CourseDao.get_course(record[4])
        reimbursement.employee = EmployeeDao.get_employee(record[1])
        reimbursement.status = ReimbursementStatusDao.get_status(record[2])
        return reimbursement

    @staticmethod
    def get_reimbursements_by_employee_id(employee_id):
        sql = "Select * from reimbursements where employee_id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        records = cursor.fetchall()
        reimbursements = []

        for record in records:
            reimbursement = Reimbursement(id=record[0], date_submitted=record[3], amount=record[5], message=record[6])
            reimbursement.course = CourseDao.get_course(record[4])
            reimbursement.employee = EmployeeDao.get_employee(record[1])
            reimbursement.status = ReimbursementStatusDao.get_status(record[2])
            reimbursements.append(reimbursement)

        return reimbursements

    @staticmethod
    def get_reimbursements_awaiting_approval(employee_id, status_id):
        sql = "Select * from reimbursements where employee_id=%s and status_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id, status_id])
        records = cursor.fetchall()
        reimbursements = []

        for record in records:
            reimbursement = Reimbursement(id=record[0], date_submitted=record[3], amount=record[5], message=record[6])
            reimbursement.course = CourseDao.get_course(record[4])
            reimbursement.employee = EmployeeDao.get_employee(record[1])
            reimbursement.status = ReimbursementStatusDao.get_status(record[2])
            reimbursements.append(reimbursement)

        return reimbursements

    @staticmethod
    def create_reimbursement(reimbursement, commit=True):
        if reimbursement.course.id is None:
            reimbursement.course.id = CourseDao.create_course(reimbursement.course)
        sql = "insert into reimbursements values (default, %s, 1, %s, %s, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement.employee.id,
                             reimbursement.date_submitted,
                             reimbursement.course.id,
                             reimbursement.amount,
                             reimbursement.message])
        connection.commit() if commit else connection.rollback()
        return True

    @staticmethod
    def update_reimbursement(id, status_id, message, amount, commit=True):
        sql = "update reimbursements set status_id = %s, message=%s, amount=%s where id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, status_id, message, amount, id)
        connection.commit() if commit else connection.rollback()
        return cursor.rowcount
