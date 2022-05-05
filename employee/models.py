from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Department(Base):
    department = models.CharField("Department", max_length=100)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self) -> str:
        return self.department


class Employee(Base):
    name = models.CharField("Name", max_length=50)
    email = models.CharField("E-mail", max_length=50, unique=True)
    department = models.ForeignKey(
        Department, 
        on_delete=models.CASCADE, 
        related_name="employee",)
    
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self) -> str:
        return self.name

