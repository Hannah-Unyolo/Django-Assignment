from django.db import models

class Class(models.Model):
    clas_id = models.SmallIntegerField()
    class_name = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    teacher = models.CharField(max_length=20)
    enrollnment = models.SmallIntegerField()
    room_number = models.SmallIntegerField()
    class_duration = models.CharField(max_length=20)
    meeting_days = models.CharField(max_length=20)
    class_rep = models.CharField(max_length=20)
    class_capacity = models.SmallIntegerField()

# Create your models here.
