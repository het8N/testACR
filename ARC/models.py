from django.db import models


# Modèle pour l'Entreprise


class Company(models.Model):
    name = models.CharField(max_length=255, null=False)  # Nom de l'entreprise, non nullable
    industry = models.CharField(max_length=255, default="Unknown", null=False)  # Secteur d'activité, non nullable

    def __str__(self):
        return self.name

# Modèle pour le Bâtiment
class Building(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='buildings', null=False)  # Lien avec l'entreprise, non nullable
    address = models.CharField(max_length=255, null=False)  # Adresse du bâtiment, non nullable

    def __str__(self):
        return f"{self.address} ({self.company.name})"

# Modèle pour le Salarié
class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees', null=False)  # Lien avec l'entreprise, non nullable
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='employees', null=False,default=0)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    job_title = models.CharField(max_length=255, null=False,default="Unknown")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.job_title})"
