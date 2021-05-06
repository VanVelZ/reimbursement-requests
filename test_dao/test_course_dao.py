import unittest
from datetime import datetime

from daos.course_dao import CourseDao
from models.course import Course


class CourseTests(unittest.TestCase):

    def get_course(self):
        return CourseDao.get_course(1)

    def create_course(self):
        return CourseDao.create_course(Course("Test name", datetime.now(), datetime.now(), 10), False)


if __name__ == '__main__':
    unittest.main()
