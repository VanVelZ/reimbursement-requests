from models.role import Role
from utils.db_connection import connection


class RoleDao:

    @staticmethod
    def get_role(id):
        sql = "Select * from roles where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        record = cursor.fetchone()
        role = Role(id=record[0], name=record[1])
        return role

