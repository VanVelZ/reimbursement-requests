from models.course_type import CourseType
from utils.db_connection import connection


class CourseTypeDao:

    @staticmethod
    def get_all_course_types():
        sql = "Select * from course_types"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        course_types = []

        for record in records:
            course_types.append(CourseType(id=record[0], name=record[1], reimbursement_percent=record[2]))

        return course_types

    @staticmethod
    def get_course_type(id):
        sql = "Select * from course_types where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        record = cursor.fetchone()
        course_type = CourseType(id=record[0], name=record[1], reimbursement_percent=record[2])
        return course_type
