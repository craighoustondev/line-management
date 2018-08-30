from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.forms.models import inlineformset_factory, model_to_dict

from .models import Meeting, Employee, Note, Action
from .forms import EmployeeForm, MeetingForm, NoteForm

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


# def meeting_edit(request, meeting_id):
#     meeting = Meeting.objects.get(pk=meeting_id)
#     MeetingInLineFormSet = inlineformset_factory(Meeting, Note, fields=('text',))
#
#     if request.method == 'POST':
#         formset = MeetingInLineFormSet(request.POST, request.FILES, instance=meeting)
#         if formset.is_valid():
#             formset.save()
#             return render(request, 'meetings/index.html')
#     else:
#         formset = MeetingInLineFormSet(instance=meeting)
#     return render(request, 'meetings/meeting_edit.html', {'formset': formset})


def meeting_edit(request, meeting_id):
    if request.method == 'POST':
        meeting = Meeting.objects.get(pk=meeting_id)
        meeting_form = MeetingForm(request.POST, instance=meeting)
        note = Note.objects.get(pk=1)
        note_form = NoteForm(request.POST, instance=note)

        if all([meeting_form.is_valid(), note_form.is_valid()]):
            meeting_form.save()
            note_form.save()
            return redirect(reverse('meetings:meetings'))
    else:
        meeting = Meeting.objects.get(pk=meeting_id)
        meeting_form = MeetingForm(instance=meeting)
        notes = Note.objects.filter(meeting=meeting)
        note_forms = []
        for note in notes:
            note_form = NoteForm(instance=note)
            note_forms.append(note_form)

    return render(request, 'meetings/meeting_edit.html', {
        'meeting_form': meeting_form,
        'note_forms': note_forms,
    })

'''
class EmployeeDetailView(generic.DetailView):
    model = Employee
    template_name = 'meetings/employee_detail.html'
'''
class MeetingDetailView(generic.DetailView):
    model = Meeting
    template_name = 'meetings/meeting_detail.html'
