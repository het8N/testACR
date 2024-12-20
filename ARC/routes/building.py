from ninja import Router
from typing import List
from ..schemas import BuildingSchema
from ..models import Building


router = Router ()


@router.post("/buildings", response=BuildingSchema)
def create_building(request, data: BuildingSchema):
    building = Building.objects.create(**data.model_dump())
    return building


@router.get("/companies/{company_id}/buildings", response=List[BuildingSchema])
def list_buildings(request, company_id: int):
    buildings = Building.objects.filter(company_id=company_id)
    return buildings


@router.get("/buildings/{building_id}", response=BuildingSchema)
def get_building(request, building_id: int):
    building = Building.objects.get(id=building_id)
    return building



@router.delete("/companies/{company_id}/buildings/{building_id}", response=BuildingSchema)
def delete_building(request, company_id: int, building_id: int):
    building = Building.objects.get(id=building_id, company_id=company_id)
    building.delete()
    return building