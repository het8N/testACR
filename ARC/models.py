from django.db import models
from ARC.constant import MAX_LENGTH

# Modèle pour l'Entreprise
class Company(models.Model):
    name: models.CharField = models.CharField(max_length=MAX_LENGTH, null=False)  # Nom de l'entreprise, non nullable
    industry: models.CharField = models.CharField(max_length=MAX_LENGTH, default="Unknown", null=False)  # Secteur d'activité, non nullable

    def __str__(self) -> str:
        return self.name


# Modèle pour le Bâtiment
class Building(models.Model):
    company: models.ForeignKey = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='buildings', null=False)  # Lien avec l'entreprise, non nullable
    address: models.CharField = models.CharField(max_length=MAX_LENGTH, null=False)  # Adresse du bâtiment, non nullable

    def __str__(self) -> str:
        return f"{self.address} ({self.company.name})"


# Modèle pour le Salarié
class Employee(models.Model):
    company: models.ForeignKey = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees', null=False)  # Lien avec l'entreprise, non nullable
    building: models.ForeignKey = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='employees', null=False, default=0)
    first_name: models.CharField = models.CharField(max_length=MAX_LENGTH, null=False)  # Prénom du salarié, non nullable
    last_name: models.CharField = models.CharField(max_length=MAX_LENGTH, null=False)  # Nom du salarié, non nullable
    job_title: models.CharField = models.CharField(max_length=MAX_LENGTH, null=False, default="Unknown")  # Poste du salarié, non nullable

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.job_title})"
