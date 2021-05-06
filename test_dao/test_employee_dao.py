import unittest

from daos.employee_dao import EmployeeDao


class EmployeeTests(unittest.TestCase):

    def test_login(self):
        employee = EmployeeDao.login('100007')
        assert employee

    def test_get_employee(self):
        assert EmployeeDao.get_employee(1)

    def test_get_supervised_employees(self):
        assert EmployeeDao.get_supervised_employees(1)

    def test_get_department_employees(self):
        assert EmployeeDao.get_employees_by_department(1)


if __name__ == '__main__':
    unittest.main()
