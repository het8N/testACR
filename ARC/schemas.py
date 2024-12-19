from pydantic import BaseModel,Field
from typing import List, Optional


# Schéma pour le modèle Company
class CompanySchema(BaseModel):
    company_id: int = Field(..., alias='id')
    name: str
    industry: str

    class Config:
        from_attributes = True  # Cela permet à Pydantic de lire les modèles Django comme des dictionnaires
        #fields = {'id':'company_id'}


# Schéma pour le modèle Building
class BuildingSchema(BaseModel):
    building_id: int = Field(..., alias='id')
    company_id: int
    address: str

    class Config:
        from_attributes = True
        #fields = {'id':'building_id'}


# Schéma pour le modèle Employee
class EmployeeSchema(BaseModel):
    employee_id: int = Field(..., alias='id')
    company_id: int
    building_id:int
    first_name: str
    last_name: str
    job_title: str

    class Config:
        from_attributes = True
        #fields = {'id':'employee_id'}
