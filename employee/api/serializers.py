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
        depart = validated_data.pop("department")

        if not depart.isupper():
            depart = depart.title()

        depart_instance, created = Department.objects.get_or_create(
            department=depart)
        employee_instance = Employee.objects.create(
            **validated_data, department=depart_instance)

        return employee_instance

