from ninja import Router
from typing import List
from django.http import HttpRequest
from ..schemas import CompanySchema
from ..models import Company

router: Router = Router()


@router.post("/companies", response=CompanySchema)
def create_company(request: HttpRequest, data: CompanySchema) -> CompanySchema:
    company: CompanySchema = Company.objects.create(**data.model_dump())
    return company


@router.get("/companies", response=List[CompanySchema])
def list_companies(request: HttpRequest) -> List[CompanySchema]:
    companies: List[CompanySchema] = Company.objects.all()
    return companies


@router.get("/companies/{company_id}", response=CompanySchema)
def get_company(request: HttpRequest, company_id: int) -> CompanySchema:
    company: CompanySchema = Company.objects.get(id=company_id)
    return company


@router.delete("/companies/{company_id}", response=CompanySchema)
def delete_company(request: HttpRequest, company_id: int) -> CompanySchema:
    company: CompanySchema = Company.objects.get(id=company_id)
    company.delete()
    return company
