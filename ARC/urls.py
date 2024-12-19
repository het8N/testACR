from .api import api
from django.urls import path, include

urlpatterns = [
    path("api/",api.urls)
]