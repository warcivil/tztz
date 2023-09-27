from django.urls import path

from employees.views import department_tree, employee_list

urlpatterns = [
    path('department_tree/', department_tree, name='department_tree'),
    path('employee_list/<int:department_id>/', employee_list, name='employee_list'),
]
