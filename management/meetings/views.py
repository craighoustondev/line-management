from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.forms.models import model_to_dict

from .models import Meeting, Employee
from .forms import EmployeeForm, MeetingForm

'''
class IndexView(generic.ListView):
    template_name = 'meetings/index.html'
    context_object_name = 'latest_meeting_list'

    def get_queryset(self):
        """Return the last five meetings."""
        return Meeting.objects.all()[:5]
'''

def index(request):
    return render(request, 'meetings/index.html')


def employees(request):
    employees = Employee.objects.all()
    return render(request, 'meetings/employees.html', {'employees': employees})


def meetings(request):
    meetings = Meeting.objects.all()
    return render(request, 'meetings/meetings.html', {'meetings': meetings})


def employee_detail(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    if request.method == 'POST':
        print('POST')
    else:
        employee_dict = model_to_dict(employee)
        form = EmployeeForm(employee_dict)

        return render(request, 'meetings/employee_detail.html', {'form':form})


def employee_edit(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    return redirect(reverse('employees'))


'''
class EmployeeDetailView(generic.DetailView):
    model = Employee
    template_name = 'meetings/employee_detail.html'
'''
class MeetingDetailView(generic.DetailView):
    model = Meeting
    template_name = 'meetings/meeting_detail.html'
