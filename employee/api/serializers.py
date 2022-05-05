from rest_framework import serializers
from employee.models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ("department",)


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.CharField()

    class Meta:
        model = Employee
        fields = ("name", "email", "department")

    def create(self, validated_data):
        """
        This method has been overridden to do the following action:
        
        Whether department field text was typed as lower case (text), 
        this if statement guarantee that the text will be as title 
        case (Text) and if all text was in upper case (TEXT), 
        this if statement will do nothing.
        """
        depart = validated_data.pop("department")

        if not depart.isupper():
            depart = depart.title()

        depart_instance, created = Department.objects.get_or_create(
            department=depart)
        employee_instance = Employee.objects.create(
            **validated_data, department=depart_instance)

        return employee_instance

