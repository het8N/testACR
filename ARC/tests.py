from django.test import TestCase
from django.forms.models import model_to_dict
from .models import Company, Building, Employee

class ModelTestCase(TestCase):

    def setUp(self):
        # Création d'une entreprise pour les tests
        self.company = Company.objects.create(
            name="TechCorp",
            industry="Technology"
        )
        # Création d'un bâtiment associé à l'entreprise
        self.building = Building.objects.create(
            company=self.company,
            address="123 Tech Street"
        )
        # Création d'un employé associé au bâtiment et à l'entreprise
        self.employee = Employee.objects.create(
            company=self.company,
            building=self.building,
            first_name="Nathan",
            last_name="Kyburz",
            job_title="Data Analyst"
        )

    def test_company_creation(self):
        """Test de la création d'une entreprise."""
        # Convertir l'entreprise en dictionnaire
        company_data = model_to_dict(self.company)
        # Supprimer l'ID du dictionnaire retourné
        company_data.pop('id')  # Supprimer l'ID

        expected_company = {
            "name": "TechCorp",
            "industry": "Technology"
        }
        # Comparer les données de l'entreprise avec celles attendues
        self.assertEqual(company_data, expected_company)

    def test_building_creation(self):
        """Test de la création d'un bâtiment."""
        # Convertir le bâtiment en dictionnaire
        building_data = model_to_dict(self.building)
        building_data.pop('id')
        expected_building = {
            "company": self.company.id,  # Le champ `company` est une relation, donc il faut comparer l'ID
            "address": "123 Tech Street"
        }
        # Comparer les données du bâtiment avec celles attendues
        self.assertEqual(building_data, expected_building)

    def test_employee_creation(self):
        """Test de la création d'un employé."""
        # Convertir l'employé en dictionnaire
        employee_data = model_to_dict(self.employee)
        # Exclure l'ID pour la comparaison
        employee_data.pop('id')  # Supprimer l'ID du dictionnaire retourné

        expected_employee = {
            "first_name": "Nathan",
            "last_name": "Kyburz",
            "job_title": "Data Analyst",
            "company": self.company.id,  # L'ID de l'entreprise
            "building": self.building.id  # L'ID du bâtiment
        }
        # Comparer les données de l'employé avec celles attendues
        self.assertEqual(employee_data, expected_employee)

    def test_relationships(self):
        """Test des relations entre les modèles."""
        self.assertIn(self.building, self.company.buildings.all())
        self.assertIn(self.employee, self.company.employees.all())
        self.assertIn(self.employee, self.building.employees.all())
