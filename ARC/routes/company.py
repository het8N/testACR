from ninja import Router
from typing import List
from ..schemas import CompanySchema
from ..models import Company

router = Router ()


@router.post("/companies", response=CompanySchema)
def create_company(request, data: CompanySchema):
    company = Company.objects.create(**data.model_dump())
    return company


@router.get("/companies", response=List[CompanySchema])
def list_companies(request):
    companies = Company.objects.all()
    return companies


@router.get("/companies/{company_id}", response=CompanySchema)
def get_company(request, company_id: int):
    company = Company.objects.get(id=company_id)
    return company


@router.delete("/companies/{company_id}", response=CompanySchema)
def delete_company(request, company_id: int):
    company = Company.objects.get(id=company_id)
    company.delete()
    return company