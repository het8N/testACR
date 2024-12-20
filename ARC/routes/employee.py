from ninja import Router
from typing import List
from django.http import HttpRequest
from ..schemas import EmployeeSchema
from ..models import Employee, Company, Building

router = Router()


@router.post("/", response=EmployeeSchema)
def create_employee(request: HttpRequest, data: EmployeeSchema) -> EmployeeSchema:
    company: Company = Company.objects.get(id=data.company_id)
    building: Building = Building.objects.get(id=data.building_id)

    employee: EmployeeSchema = Employee.objects.create(
        company=company,
        building=building,
        first_name=data.first_name,
        last_name=data.last_name,
        job_title=data.job_title,
    )

    return employee


@router.get("/", response=List[EmployeeSchema])
def list_employees(request: HttpRequest, company_id: int) -> List[EmployeeSchema]:
    employees: List[EmployeeSchema] = Employee.objects.filter(company_id=company_id)
    return employees


@router.get("/{employee_id}", response=EmployeeSchema)
def get_employee(request: HttpRequest, employee_id: int) -> EmployeeSchema:
    employee: EmployeeSchema = Employee.objects.get(id=employee_id)
    return employee


@router.delete("/{employee_id}", response=EmployeeSchema)
def delete_employee(request: HttpRequest, employee_id: int) -> EmployeeSchema:
    employee: EmployeeSchema = Employee.objects.get(id=employee_id)
    employee.delete()
    return employee
