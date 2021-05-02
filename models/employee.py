
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
        self.reimbursements = []
        self.department_employees_reimbursements = []
        self.supervised_employees_reimbursements = []

    def serialize(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "department": self.department.serialize(),
            "role": self.role.serialize(),
            "supervisor": self.supervisor.serialize(),
            "reimbursements": self._get_reimbursements_as_json(self.reimbursements),
            "supervisedReimbursements": self._get_reimbursements_as_json(self.supervised_employees_reimbursements),
            "departmentReimbursements": self._get_reimbursements_as_json(self.department_employees_reimbursements)

        }

    @staticmethod
    def _get_reimbursements_as_json(reimbursements):
        jsons = []
        for reimbursement in reimbursements:
            jsons.append(reimbursement.serialize())
        return jsons
