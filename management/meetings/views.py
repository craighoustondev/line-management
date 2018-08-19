from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from .models import Meeting

# Create your views here.
def index(request):
    latest_meeting_list = Meeting.objects.all()
    context = {
        'latest_meeting_list': latest_meeting_list
    }
    return render(request, 'meetings/index.html', context)

def employee_detail(request, employee_id):
    return HttpResponse("Details for employee %s." % employee_id)

def meeting_detail(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    return render(request, 'meetings/meeting_detail.html', {'meeting': meeting})