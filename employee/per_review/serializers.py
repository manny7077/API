from rest_framework.serializers import ModelSerializer
from .models import Employee_Result, Measure

class Employee_ResultSerializer(ModelSerializer):
    class Meta:
        model = Employee_Result
        fields = '__all__'
        
        
class MeasureSerializer(ModelSerializer):
  
    class Meta:
        model= Measure
        fields = '__all__'