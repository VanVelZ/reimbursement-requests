from daos.employee_dao import EmployeeDao
from daos.reimbursement_dao import ReimbursementDao

class EmployeeService:

    @staticmethod
    def login(login_id):
        employee = EmployeeDao.login(login_id)
        _get_reimbursements_needing_attention(employee)
        return employee


def _get_reimbursements_needing_attention(employee):
    employee.reimbursements_needing_attention = ReimbursementDao.get_reimbursements_awaiting_approval(employee.id, 7)
    employee.reimbursements_needing_attention += ReimbursementDao.get_reimbursements_awaiting_approval(employee.id, 5)
    if employee.department.head == employee.id:
        department_employees = EmployeeDao.get_employees_by_department(employee.department.id)
        for emp in department_employees:
            employee.reimbursements_needing_attention += \
                ReimbursementDao.get_reimbursements_awaiting_approval(emp.id, 2)
    supervised_employees = EmployeeDao.get_supervised_employees(employee.id)
    for emp in supervised_employees:
        employee.reimbursements_needing_attention += \
            ReimbursementDao.get_reimbursements_awaiting_approval(emp.id, 1)
