from daos.employee_dao import EmployeeDao
from models.department import Department
from utils.db_connection import connection


class DepartmentDao:

    @staticmethod
    def get_all_departments():
        sql = "Select * from departments"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        departments = []

        for record in records:
            department = Department(id=record[0], name=record[1])
            if record[2] is not None:
                department.head = EmployeeDao.get_employee(record[2])
            departments.append(department)

        return departments

    @staticmethod
    def get_department(id):
        sql = "Select * from departments where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        record = cursor.fetchone()
        department = Department(id=record[0], name=record[1])
        if record[2] is not None:
            department.head = EmployeeDao.get_employee(record[2])

        return department

