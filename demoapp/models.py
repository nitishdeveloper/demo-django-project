from django.db import models

class Employee(models.Model) :
    eid = models.CharField(max_length=100)
    fullname = models.CharField(max_length=20)
    email = models.EmailField()
    contact = models.CharField(max_length=30)