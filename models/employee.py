from models.department import Department
from models.role import Role


class Employee:

    def __init__(self,
                 first_name,
                 last_name,
                 login_id,
                 department=None,
                 role=None,
                 supervisor=None,
                 id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.login_id = login_id
        self.department = department
        self.role = role
        self.supervisor = supervisor
        self.id = id
        self.reimbursements_needing_attention = []
        self.total_reimbursements_this_year = 0

    def serialize(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "loginId": self.login_id,
            "lastName": self.last_name,
            "department": self.department.serialize(),
            "role": self.role.serialize(),
            "supervisor": self.supervisor.serialize() if self.supervisor else None,
            "reimbursements": self._get_reimbursements_as_json(self.reimbursements_needing_attention),
            "totalReimbursements": str(self.total_reimbursements_this_year)
        }
    @staticmethod
    def deserialize(json):
        return Employee(id=json["id"],
                        login_id=json["loginId"],
                        first_name=json["firstName"],
                        last_name=json["lastName"],
                        department=Department.deserialize(json["department"]),
                        role=Role.deserialize(json["role"]),
                        supervisor=Employee.deserialize(json["supervisor"]) if json["supervisor"] else None)

    @staticmethod
    def _get_reimbursements_as_json(reimbursements):
        jsons = []
        for reimbursement in reimbursements:
            jsons.append(reimbursement.serialize())
        return jsons
