from ninja import Router
from typing import List
from ..schemas import EmployeeSchema
from ..models import Employee

router = Router()


@router.post("/employees", response=EmployeeSchema)
def create_employee(request, data: EmployeeSchema):
    company = Company.objects.get(id=data.company_id)
    building = Building.objects.get(id=data.building_id)

    employee = Employee.objects.create(
        company=company,
        building=building,
        first_name=data.first_name,
        last_name=data.last_name,
        job_title=data.job_title,
    )

    return employee


@router.get("/companies/{company_id}/employees", response=List[EmployeeSchema])
def list_employees(request, company_id: int):
    employees = Employee.objects.filter(company_id=company_id)
    return employees


@router.get("/employees/{employee_id}", response=EmployeeSchema)
def get_employee(request, employee_id: int):
    employee = Employee.objects.get(id=employee_id)
    return employee



@router.delete("/employees/{employee_id}", response=EmployeeSchema)
def delete_employee(request, employee_id: int):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    return employee