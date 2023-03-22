import uuid

from django.db import models


# Create your models here.

class Recruiter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)


class Candidate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    applying_position = models.CharField(max_length=100)
    cv_link = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)


class Interview(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    interview_type = models.IntegerField()
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField('appointment date')
    appointment_link = models.CharField(max_length=200)
    notes = models.CharField(max_length=300)

    def __str__(self):
        return str(self.id)
