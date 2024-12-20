# ARC/urls.py

from django.urls import path
from ninja import NinjaAPI
from .routes.company import router as company_router
from .routes.building import router as building_router
from .routes.employee import router as employee_router

api = NinjaAPI()

# Ajouter les routeurs de chaque fichier de routes
api.add_router("/companies/", company_router)
api.add_router("/buildings/", building_router)
api.add_router("/employees/", employee_router)

urlpatterns = [
    path("api/", api.urls),  # Définit tous les endpoints avec le préfixe "/api"
]
