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

    @staticmethod
    def update_course_type(changing_course_type):
        sql = "Update course_types set name=%s, reimbursement_percent=%s where id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [changing_course_type.name,
                             changing_course_type.reimbursement_percent,
                             changing_course_type.id])
        connection.commit()
        return changing_course_type

    @staticmethod
    def delete_course_type(id):
        sql = "Delete from course_types where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        connection.commit()
        return cursor.rowcount

    @staticmethod
    def create_course_type(course_type):
        sql = "Insert into course_types values (default, %s)"
        cursor = connection.cursor()
        cursor.execute(sql, [course_type.name])
        connection.commit()
        return True
