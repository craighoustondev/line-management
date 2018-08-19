from django.urls import path
from . import views

app_name = 'meetings'
urlpatterns = [
    # ex: /meetings/
    path('', views.index, name='index'),
    # ex: /meetings/employee/5/
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    # ex: /meetings/meeting/5/
    path('meeting/<int:meeting_id>/', views.meeting_detail, name='meeting_detail'),
]