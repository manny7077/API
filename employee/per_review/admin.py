from django.contrib import admin
from .models import Employee_Result, Measure



class Employee_ResultAdmin(admin.ModelAdmin):
    list_display = ('employee_results',)  
    


class MeasureAdmin(admin.ModelAdmin):
    list_display = ('employee', 'measure', 'target', 'weight', 'actual', 'rating', 'rating_weight', 'remark', )

admin.site.register(Employee_Result, Employee_ResultAdmin)
admin.site.register(Measure, MeasureAdmin)
