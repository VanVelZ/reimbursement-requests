import unittest

from daos.employee_dao import EmployeeDao


class MyTestCase(unittest.TestCase):
    def test_login(self):
        employee = EmployeeDao.login('100007')
        assert employee


if __name__ == '__main__':
    unittest.main()
