from django.contrib import admin
from employee.models import Employee, Department


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'department',
        'created_at',
        'active')
    list_filter = ('created_at', 'department')
    search_fields = ('email', 'department')


admin.site.register(Employee, EmployeeAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'department','created_at','active')
    list_filter = ('created_at', 'department')
    search_fields = ('department',)


admin.site.register(Department, DepartmentAdmin)
