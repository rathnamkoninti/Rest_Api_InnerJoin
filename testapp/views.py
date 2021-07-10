from django.shortcuts import render
from testapp.models import Employee,Company
from testapp.serializers import EmployeeSerializer,CompanySerializer
# Create your views here.

from rest_framework.viewsets import ModelViewSet
# class MyImage(ModelViewSet):
#     queryset = MyImages.objects.all()
#     serializer_class = MyImageSerializers

class MyModelView(ModelViewSet):
    queryset = Employee.objects.raw(" SELECT  testapp_Employee.emp_id,testapp_Employee.name,testapp_Company.cmp_id,testapp_Company.cname FROM testapp_Employee JOIN testapp_Company ON testapp_Employee.emp_id=testapp_Company.cmp_id")
    # queryset = Employee.objects.raw("SELECT * FROM testapp_Employee")
    print(queryset)
    for q in queryset:
        print(q.name,q.emp_id,q.mbl,q.cmp_id,q.cname)


    serializer_class = CompanySerializer
    serializer_class = EmployeeSerializer
    # serializer_class = CompanySerializer
