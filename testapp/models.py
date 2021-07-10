from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    mbl = models.IntegerField()

    def __str__(self):
        return self.name


class Company(models.Model):
    cmp_id = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=60)

    def __str__(self):
        return self.cname
