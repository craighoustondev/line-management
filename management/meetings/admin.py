from django.contrib import admin
from .models import Employee, Meeting, EmployeeMeeting, Relationship, Note, Action

admin.site.register(Employee)
admin.site.register(Meeting)
admin.site.register(EmployeeMeeting)
admin.site.register(Relationship)
admin.site.register(Note)
admin.site.register(Action)
