from django.http import Http404
from employee.models import Employee
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from employee.api.serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import (
    SessionAuthentication, BasicAuthentication)


class EmployeeListCreateDestroyViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):

    queryset = Employee.objects.all().order_by("id")
    serializer_class = EmployeeSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_renderer_context(self):
        """
        Overriding this method to render indented in terminal
        """
        context = super().get_renderer_context()
        context["indent"] = 4
        return context

    def destroy(self, request, *args, **kwargs):
        """
        Overriding this method to render 
        with success or error message
        """
        try:
            employee = self.get_object()
            self.perform_destroy(employee)

            return Response(
                {"message":"Employee deleted successfully"},
                status=status.HTTP_204_NO_CONTENT)
        except Http404:

            return Response(
                {"error":"Employee not found"}, 
                status=status.HTTP_404_NOT_FOUND)

