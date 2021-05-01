class Employee:

    def __init__(self,
                 first_name,
                 last_name,
                 login_id,
                 department=None,
                 role="Unassigned",
                 supervisor=None,
                 id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.login_id = login_id
        self.department = department
        self.role = role
        self.supervisor = supervisor
        self.id = id
        self.department_employees = []
        self.supervised_employees = []

