from ninja import NinjaAPI
from .models import Company, Building, Employee
from django.forms.models import model_to_dict
from .schemas import CompanySchema, BuildingSchema, EmployeeSchema
from typing import List

api = NinjaAPI()

# Routes GET, POST, PUT, DELETE pour Company, Building, Employee

## Companies


@api.post("/companies", response=CompanySchema)
def create_company(request, data: CompanySchema):
    company = Company.objects.create(**data.model_dump())
    return company


@api.get("/companies", response=List[CompanySchema])
def list_companies(request):
    companies = Company.objects.all()
    return companies


@api.get("/companies/{company_id}", response=CompanySchema)
def get_company(request, company_id: int):
    company = Company.objects.get(id=company_id)
    return company


@api.delete("/companies/{company_id}", response=CompanySchema)
def delete_company(request, company_id: int):
    company = Company.objects.get(id=company_id)
    company.delete()
    return company


## Buildings

@api.post("/buildings", response=BuildingSchema)
def create_building(request, data: BuildingSchema):
    building = Building.objects.create(**data.model_dump())
    return building


@api.get("/companies/{company_id}/buildings", response=List[BuildingSchema])
def list_buildings(request, company_id: int):
    buildings = Building.objects.filter(company_id=company_id)
    return buildings


@api.get("/buildings/{building_id}", response=BuildingSchema)
def get_building(request, building_id: int):
    building = Building.objects.get(id=building_id)
    return building



@api.delete("/companies/{company_id}/buildings/{building_id}", response=BuildingSchema)
def delete_building(request, company_id: int, building_id: int):
    building = Building.objects.get(id=building_id, company_id=company_id)
    building.delete()
    return building


## Employee


@api.post("/employees", response=EmployeeSchema)
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


@api.get("/companies/{company_id}/employees", response=List[EmployeeSchema])
def list_employees(request, company_id: int):
    employees = Employee.objects.filter(company_id=company_id)
    return employees


@api.get("/employees/{employee_id}", response=EmployeeSchema)
def get_employee(request, employee_id: int):
    employee = Employee.objects.get(id=employee_id)
    return employee



@api.delete("/employees/{employee_id}", response=EmployeeSchema)
def delete_employee(request, employee_id: int):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    return employee




