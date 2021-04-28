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
            roles.append()

        return roles

    @staticmethod
    def get_role(id):
        sql = "Select id, name from roles where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        record = cursor.fetchone()
        try:
            role = Role()
            return role
        except TypeError as e:
            return False

    @staticmethod
    def update_role(changing_role):
        sql = "Update roles set name=%s where id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [changing_role.name, changing_role.id])
        connection.commit()
        return cursor.rowcount

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