import unittest

from daos.course_type_dao import CourseTypeDao
from daos.department_dao import DepartmentDao
from daos.grading_format_dao import GradingFormatDao
from daos.reimbursement_status_dao import ReimbursementStatusDao
from daos.role_dao import RoleDao


class GeneralTests(unittest.TestCase):

    def test_course_type(self):
        assert CourseTypeDao.get_course_type(1)

    def test_department(self):
        assert DepartmentDao.get_department(1)

    def test_grading_format(self):
        assert GradingFormatDao.get_format(1)

    def test_reimbursement_status(self):
        assert ReimbursementStatusDao.get_status(1)

    def role_dao(self):
        assert RoleDao.get_role(1)
        

if __name__ == '__main__':
    unittest.main()