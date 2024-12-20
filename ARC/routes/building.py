from ninja import Router
from typing import List
from django.http import HttpRequest
from ..schemas import BuildingSchema
from ..models import Building


router = Router()


@router.post("/", response=BuildingSchema)
def create_building(request: HttpRequest, data: BuildingSchema) -> BuildingSchema:
    building: BuildingSchema = Building.objects.create(**data.model_dump(exclude_unset=True))
    return building


@router.get("/", response=List[BuildingSchema])
def list_buildings(request: HttpRequest, company_id: int) -> List[BuildingSchema]:
    buildings: List[BuildingSchema] = Building.objects.filter(company_id=company_id)
    return buildings


@router.get("/{building_id}", response=BuildingSchema)
def get_building(request: HttpRequest, building_id: int) -> BuildingSchema:
    building: BuildingSchema = Building.objects.get(id=building_id)
    return building
