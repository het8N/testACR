from django.test import TestCase

# Create your tests here.


from django.test import TestCase
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
        self.assertEqual(self.company.name, "TechCorp")
        self.assertEqual(self.company.industry, "Technology")

    def test_building_creation(self):
        """Test de la création d'un bâtiment."""
        self.assertEqual(self.building.address, "123 Tech Street")
        self.assertEqual(self.building.company, self.company)

    def test_employee_creation(self):
        """Test de la création d'un employé."""
        self.assertEqual(self.employee.first_name, "Nathan")
        self.assertEqual(self.employee.last_name, "Kyburz")
        self.assertEqual(self.employee.job_title, "Data Analyst")
        self.assertEqual(self.employee.company, self.company)
        self.assertEqual(self.employee.building, self.building)

    def test_relationships(self):
        """Test des relations entre les modèles."""
        self.assertIn(self.building, self.company.buildings.all())
        self.assertIn(self.employee, self.company.employees.all())
        self.assertIn(self.employee, self.building.employees.all())
