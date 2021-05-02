from daos.employee_dao import EmployeeDao


class EmployeeService:

    @staticmethod
    def login(login_id):
        return EmployeeDao.login(login_id)
