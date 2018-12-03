from django.db import models
from django.utils import timezone

class Staff(models.Model):
    staff_name = models.CharField(max_length=250)
    staff_email = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.staff_name

class Visitor(models.Model):
    visitor_name = models.CharField(max_length=250)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}'.format(self.visitor_name)

class VisitRequest(models.Model):
    staff=models.ForeignKey(Staff, on_delete=models.CASCADE)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    reason = models.TextField(default='')
    token=models.CharField(max_length=20)
    status= models.NullBooleanField()
