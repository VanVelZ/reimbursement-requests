from models.role import Role
from utils.db_connection import connection


class RoleDao:

    @staticmethod
    def get_all_roles():
        sql = "Select * from roles"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        roles = []

        for record in records:
            roles.append(Role(id=record[0], name=record[1]))

        return roles

    @staticmethod
    def get_role(id):
        sql = "Select * from roles where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        record = cursor.fetchone()
        role = Role(id=record[0], name=record[1])
        return role

    @staticmethod
    def update_role(changing_role):
        sql = "Update roles set name=%s where id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [changing_role.name, changing_role.id])
        connection.commit()
        return changing_role

    @staticmethod
    def delete_role(id):
        sql = "Delete from roles where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        connection.commit()
        return cursor.rowcount

    @staticmethod
    def create_role(role):
        sql = "Insert into roles values (default, %s)"
        cursor = connection.cursor()
        cursor.execute(sql, [role.name])
        connection.commit()
        return True
