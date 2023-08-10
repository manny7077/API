from django.db import models

# Create your models here.
class Employee_Result(models.Model):
    employee_results = models.TextField()
    
    def __str__(self):
        return self.employee_results


class Measure(models.Model):
    employee = models.ForeignKey(Employee_Result, on_delete=models.CASCADE, related_name='measures')
    measure = models.TextField(blank=True, null=True)
    target = models.CharField(max_length=20, blank=True, null=True)
    weight = models.CharField(max_length=10, blank=True, null=True)
    actual = models.CharField(max_length=20, blank=True, null=True)
    rating = models.CharField(blank=True, null =True, max_length=3)
    rating_weight = models.CharField(blank=True, null=True, max_length=3)
    remark = models.TextField()

    def __str__(self):
        return self.measure

