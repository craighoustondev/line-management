from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    position = models.CharField(max_length=50)

    @property
    def full_name(self):
        """Returns the person's full name."""
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return self.full_name


class Relationship(models.Model):
    parent = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='parent_relationship')
    child = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='child_relationship')

    def __str__(self):
        return '%s : %s' % (self.parent, self.child)


class Meeting(models.Model):
    ONE_TO_ONE = '121'
    PDR = 'PDR'
    MEETING_TYPE_CHOICES = (
        (ONE_TO_ONE, 'One to One'),
        (PDR, 'PDR'),
    )

    date = models.DateTimeField()
    type = models.CharField(max_length=10, choices=MEETING_TYPE_CHOICES, default=ONE_TO_ONE)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class EmployeeMeeting(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    meeting = models.ForeignKey(Meeting, on_delete=models.PROTECT)

    def __str__(self):
        return '%s : %s' % (self.employee, self.meeting)


class Note(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.PROTECT)
    text = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.text


class Action(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.PROTECT)
    text = models.CharField(max_length=200, blank=True, null=True)
    employee_to_action = models.ForeignKey(Employee, on_delete=models.PROTECT)
    date_to_be_actioned = models.DateField()

    def __str__(self):
        return self.text
