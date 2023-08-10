from rest_framework import generics
from .models import Employee_Result, Measure
from .serializers import Employee_ResultSerializer, MeasureSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


@api_view(['GET'])
def index(request):
    return Response({'message': 'Welcome to the API'})


class Employee_ResultListCreateView(generics.ListCreateAPIView):
    queryset = Employee_Result.objects.all()
    serializer_class = Employee_ResultSerializer


class Employee_ResultDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee_Result.objects.all()
    serializer_class = Employee_ResultSerializer


class MeasureListCreateView(generics.ListCreateAPIView):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer

class MeasureDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer
   




@api_view(['GET'])
def get_measures_for_employee_result(request, employee_result_id):
    try:
        employee_result = Employee_Result.objects.get(id=employee_result_id)
        measures = Measure.objects.filter(employee=employee_result)
        serializer = MeasureSerializer(measures, many=True)
        return Response(serializer.data)
    except Employee_Result.DoesNotExist:
        return Response({"message": "Employee_Result not found."}, status=404)



