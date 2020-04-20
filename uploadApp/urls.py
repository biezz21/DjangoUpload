from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.upload_vcf, name='upload_vcf'),
    path('list/', views.vcf_list, name='vcf_list'),
]