from django.urls import path
from . import views

app_name = 'meetings'
urlpatterns = [
    # ex: /meetings/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /meetings/employee/5/
    # path('employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    # ex: /meetings/meeting/5/
    path('meeting/<int:pk>/', views.MeetingDetailView.as_view(), name='meeting_detail'),

    path('employees/', views.employees, name='employees'),
    path('employee/<int:employee_id>/edit/', views.employee_edit, name='employee_edit'),
]