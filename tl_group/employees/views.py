from django.shortcuts import render
from .models import Department, Employee

def department_tree(request):
    departments = Department.objects.all()
    return render(request, 'department_tree.html', {'departments': departments})

def employee_list(request, department_id):
    department = Department.objects.get(pk=department_id)
    employees = Employee.objects.filter(department=department)
    return render(request, 'employee_list.html', {'department': department, 'employees': employees})
