"""hfam_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from .views.ageDistribution import AgeDistributionList, AgeDistributionDetail
from .views.disease import DiseaseList, DiseaseDetail
from .views.doctor import DoctorList, DoctorDetail
from .views.hospital import HospitalList, HospitalDetail
from .views.inventory import InventoryList, InventoryDetail
from .views.patient import PatientList, PatientDetail
from .views.predictionInputs import PredictionInputsList, PredictionInputsDetail
from .views.predictionOutputs import PredictionOutputsList, PredictionOutputsDetail
from .views.region import RegionList, RegionDetail
from .views.timetable import TimeTableList, TimeTableDetail
from .views.predictionOutputViaInput import get_prediction_output_via_input

urlpatterns = [
    path("agedistributions/", AgeDistributionList.as_view(), name="ageDistribution"),
    path("agedistributions/<int:pk>/", AgeDistributionDetail.as_view(), name="ageDistribution"),
    path("hospitals/", HospitalList.as_view(), name="hospital"),
    path("hospitals/<int:pk>/", HospitalDetail.as_view(), name="hospital"),
    path("doctors/", DoctorList.as_view(), name="doctor"),
    path("doctors/<int:pk>/", DoctorDetail.as_view(), name="doctor"),
    path("regions/", RegionList.as_view(), name="region"),
    path("regions/<int:pk>/", RegionDetail.as_view(), name="region"),
    path("diseases/", DiseaseList.as_view(), name="disease"),
    path("diseases/<int:pk>/", DiseaseDetail.as_view(), name="disease"),
    path("inventories/", InventoryList.as_view(), name="inventory"),
    path("inventories/<int:pk>/", InventoryDetail.as_view(), name="inventory"),
    path("patients/", PatientList.as_view(), name="patient"),
    path("patients/<int:pk>/", PatientDetail.as_view(), name="patient"),
    path("timetables/", TimeTableList.as_view(), name="timetable"),
    path("timetables/<int:pk>/", TimeTableDetail.as_view(), name="timetable"),
    path("predictioninputs/", PredictionInputsList.as_view(), name="predictioninputs"),
    path("predictioninputs/<int:pk>/", PredictionInputsDetail.as_view(), name="predictioninputs"),
    path("predictionoutputs/", PredictionOutputsList.as_view(), name="predictionoutputs"),
    path("predictionoutputs/<int:pk>/", PredictionOutputsDetail.as_view(), name="predictionoutputs"),
    path("predictionoutputs/input/<int:p_inputs_k>", get_prediction_output_via_input, name="getPredictionOutputsViaInput")
]
