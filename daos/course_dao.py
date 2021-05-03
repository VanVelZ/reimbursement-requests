from datetime import datetime

from daos.course_type_dao import CourseTypeDao
from daos.grading_format_dao import GradingFormatDao
from models.course import Course
from models.course_type import CourseType
from models.grading_format import GradingFormat
from utils.db_connection import connection


class CourseDao:

    @staticmethod
    def get_all_courses():
        sql = "Select * from courses"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        courses = []

        for record in records:
            course = Course(id=record[0], name=record[1], start_date=record[3], end_date=record[4], cost=record[6])
            course.type = CourseTypeDao.get_course_type(record[2])
            course.grading_format = GradingFormatDao.get_format(record[5])
            courses.append(course)

        return courses

    @staticmethod
    def get_course(id):
        sql = "Select * from course_types where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        record = cursor.fetchone()
        course = Course(id=record[0], name=record[1], start_date=record[3], end_date=record[4], cost=record[6])
        course.type = CourseTypeDao.get_course_type(record[2])
        course.grading_format = GradingFormatDao.get_format(record[5])
        return course

    @staticmethod
    def create_course(course, commit=True):
        sql = "insert into courses values (default, %s, %s, %s, %s, %s, %s) Returning id"
        cursor = connection.cursor()
        cursor.execute(sql, [course.name, course.type.id, course.start_date, course.end_date, course.grading_format.id,
                       course.cost])
        connection.commit() if commit else connection.rollback()
        return cursor.fetchone()


