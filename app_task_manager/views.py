from .models import Assignment
from .serializers import (
    AssignmentSerializer,
    UpdateAssignmentSerializer,
    UpdateAssignmentStatusSerializer)

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view


class Health(APIView):
    """Health Check"""

    def get(self, request):
        return Response({"message": "ok"}, status=status.HTTP_200_OK)


class AssignmentView(APIView):
    @swagger_auto_schema(operation_description='')
    def get(self, request, id_task=None):
        """ get all o one task"""
        if id_task:
            documents = Assignment.objects.filter(id=id_task)
            serializer = AssignmentSerializer(documents, many=True)
        else:
            documents = Assignment.objects.all()
            serializer = AssignmentSerializer(documents, many=True)
        return Response(serializer.data)


@swagger_auto_schema(method='POST', request_body=AssignmentSerializer)
@api_view(['POST'])
def create_task(request):
    """
    Creates new task
    """
    serializer = AssignmentSerializer(data=request.data, partial=True)
    if not serializer.is_valid():
        return Response(
            {
                "success": False,
                "code": 400,
                "message": "The request is not valid",
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    create_assignment = Assignment(
        title=serializer.data['title'],
        description=serializer.data['description'],
        status=serializer.data['status'],
    )
    create_assignment.save()

    return Response(
        {
            "success": True,
            "code": 200,
            "assignment": serializer.data,
        },
        status=status.HTTP_200_OK
    )


class AssignmentTranView(APIView):

    @swagger_auto_schema(request_body=UpdateAssignmentSerializer)
    def put(self, request, id_task):
        """Update task"""
        product = Assignment.objects.get(id=id_task)
        update_seriailizer = UpdateAssignmentSerializer(product, data=request.data, partial=True)
        if update_seriailizer.is_valid():
            update_seriailizer.save()
            return Response(
                {
                    "success": True,
                    "code": 200,
                    "task": update_seriailizer.data,
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                "success": False,
                "code": 400,
                "message": "The request is not valid",
            },
            status=status.HTTP_400_BAD_REQUEST
        )



    @swagger_auto_schema( request_body=UpdateAssignmentStatusSerializer)
    def patch(self, request, id_task):
        """Update only status task"""
        product = Assignment.objects.get(id=id_task)
        update_seriailizer = UpdateAssignmentStatusSerializer(product, data=request.data)
        if update_seriailizer.is_valid():
            update_seriailizer.save()
            return Response(
                {
                    "success": True,
                    "code": 200,
                    "task": update_seriailizer.data
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                "success": False,
                "code": 400,
                "message": "The data is not valid",
            },
            status=status.HTTP_400_BAD_REQUEST
        )



    @swagger_auto_schema(method='DELETE')
    def delete(self, request, id_task):
        """Deleted task"""
        get_object_or_404(Assignment, id=id_task)

        if not AssignmentSerializer(Assignment.objects.filter(id=id_task)).data:
            return Response(
                {
                    "success": False,
                    "code": 400,
                    "message": "The request is not valid",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        Assignment.objects.filter(id=id_task).delete()
        return Response(
            {
                "success": True,
                "code": 200,
                "message": "Assignment was delete"
            },
            status=status.HTTP_200_OK
        )






