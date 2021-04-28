from models.grading_format import GradingFormat
from utils.db_connection import connection


class GradingFormatDao:

    @staticmethod
    def get_all_formats():
        sql = "Select * from grading_formats"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        formats = []

        for record in records:
            formats.append(GradingFormat(id=record[0], type=record[1], requires_presentation=record[2]))

        return formats

    @staticmethod
    def get_format(id):
        sql = "Select * from grading_formats where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        record = cursor.fetchone()
        format = GradingFormat(id=record[0], type=record[1], requires_presentation=record[2])
        return format
