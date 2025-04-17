from django.core import exceptions
from django.db import models
from curricula import models as cmodels
from students import models as smodels
# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=250)
    term = models.ForeignKey(
        cmodels.Term, on_delete=models.CASCADE, related_name="groups")
    students = models.ManyToManyField(smodels.Student, related_name="students")
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        # Only check if instance is saved and has students
        if self.pk and self.students.count() > 6:
            raise exceptions.ValidationError(
                "A group cannot have more than 6 students.")

    def __str__(self):
        return f"{self.name} | {self.term}"


class Tutorial(models.Model):
    title = models.CharField(max_length=250)
    meeting_link = models.URLField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.title} | {self.date.isoformat()}, {self.start_time.isoformat()}"
