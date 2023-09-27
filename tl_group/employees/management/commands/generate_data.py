import random
from django.core.management.base import BaseCommand
from employees.models import Department, Employee
from faker import Faker

class Command(BaseCommand):
    help = 'Генерация случайных данных для сотрудников и подразделений'

    def handle(self, *args, **kwargs):
        fake = Faker()
        root_department = Department.objects.create(name='Генеральное управление', parent=None)
        self.generate_departments(fake, root_department, 5, 5)
        self.generate_employees(fake, root_department, 50000)

    def generate_departments(self, fake, parent, max_levels, max_children):
        if max_levels == 0:
            return

        num_children = random.randint(1, max_children)
        for _ in range(num_children):
            name = fake.unique.company()
            department = Department.objects.create(name=name, parent=parent)
            self.generate_departments(fake, department, max_levels - 1, max_children)

    def generate_employees(self, fake, department, num_employees):
        for _ in range(num_employees):
            full_name = fake.name()
            position = fake.job()
            hire_date = fake.date_between(start_date='-5y', end_date='today')
            salary = round(random.uniform(30000, 80000), 2)
            Employee.objects.create(
                full_name=full_name,
                position=position,
                hire_date=hire_date,
                salary=salary,
                department=department
            )
