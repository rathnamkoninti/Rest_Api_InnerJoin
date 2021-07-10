from rest_framework import serializers
from testapp.models import  Employee,Company
from django.forms.fields import FileField


# class MyImageSerializers(serializers.HyperlinkedModelSerializer):
#     file = serializers.FileField(max_length=None, allow_empty_file=False, use_url=True)
#     class Meta:
#         model = MyImages
#         fields = ('title','file')

class EmployeeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Employee
        fields = "__all__"

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
#
# class ProjectSerializer(serializers.ModelSerializer):
#     project_by = serializers.ReadOnlyField(source='project_by.user_name')
#     project_by_id = serializers.ReadOnlyField(source='project_by.id')
#     project_by_email = serializers.ReadOnlyField(source='project_by.email')
#     project_by_First_Name = serializers.ReadOnlyField(source='project_by.first_name')
#
#
#     class Meta:
#         model = Project
#         fields = ['id','project_name', 'project_by_id','project_by','project_by_email','project_by_First_Name']
