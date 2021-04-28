from daos.department_dao import DepartmentDao
from daos.role_dao import RoleDao
from models.employee import Employee
from utils.db_connection import connection


class EmployeeDao:

    @staticmethod
    def get_all_employees():
        sql = "Select * from employees"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        employees = []

        for record in records:
            employee = Employee(id=record[0], first_name=record[1], last_name=record[2], login_id=record[3])
            employee.department = DepartmentDao.get_department(record[4])
            employee.role = RoleDao.get_role(record[5])
            if record[6] is not None:
                employee.supervisor = EmployeeDao.get_employee(record[6])

        return employees

    @staticmethod
    def get_employee(id):
        sql = "Select * from employees where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        record = cursor.fetchone()
        employee = Employee(id=record[0], first_name=record[1], last_name=record[2], login_id=record[3])
        employee.department = DepartmentDao.get_department(record[4])
        employee.role = RoleDao.get_role(record[5])
        if record[6] is not None:
            employee.supervisor = EmployeeDao.get_employee(record[6])
        return employee

    @staticmethod
    def login(login_id):
        sql = "Select * from employees where login_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [login_id])
        record = cursor.fetchone()
        if record:
            employee = Employee(id=record[0], first_name=record[1], last_name=record[2], login_id=record[3])
            employee.department = DepartmentDao.get_department(record[4])
            employee.role = RoleDao.get_role(record[5])
            if record[6] is not None:
                employee.supervisor = EmployeeDao.get_employee(record[6])
            return employee
        else:
            return False
