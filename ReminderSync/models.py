from django.db import models

class Reminder(models.Model):
    timestamp = models.DateTimeField()
    assignee = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    task = models.CharField(max_length=255)
    deadline = models.DateField()
    completed_date = models.DateField(null=True, blank=True)
    repeat = models.CharField(max_length=10)
    completed = models.CharField(max_length=10)
