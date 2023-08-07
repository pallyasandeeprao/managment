from django.db import models
#employee managment
# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100,null=False)
    location=models.CharField(max_length=40)
    def __str__(self):
        return self.name
class Role(models.Model):
    name=models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.name
class Employe(models.Model):
    first_name=models.CharField(max_length=40,null=False)
    last_name=models.CharField(max_length=40)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.IntegerField()
    bonus=models.IntegerField()
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.BigIntegerField()
    hire_date=models.DateField()

    def __str__(self):
        return self.first_name