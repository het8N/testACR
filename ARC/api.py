from ninja import NinjaAPI
from .routes import company,building,employee


api = NinjaAPI()

# Routes GET, POST, PUT, DELETE pour Company, Building, Employee

api.add_router("/companies", company.router)
api.add_router("/buildings", building.router)
api.add_router("/employees", employee.router)
