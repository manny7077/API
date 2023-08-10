"""
URL configuration for employee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from per_review.views import index, Employee_ResultListCreateView, Employee_ResultDetailView, MeasureListCreateView,MeasureDetailView, get_measures_for_employee_result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('employee_results/', Employee_ResultListCreateView.as_view(), name='employee_results_list_create'),
    path('employee_results/<int:pk>/', Employee_ResultDetailView.as_view(), name='employee_result_detail'),
    path('measures/', MeasureListCreateView.as_view(), name='measure_list'),
    path('measures/<int:pk>/', MeasureDetailView.as_view(), name='measure_detail'),
    path('employee_results/<int:employee_result_id>/measures/', get_measures_for_employee_result, name='get_measures_for_employee_result'),
]