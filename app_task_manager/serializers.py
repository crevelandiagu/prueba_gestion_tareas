from rest_framework import serializers
from app_task_manager.models import Assignment
from .helpers import STATUS


class AssignmentSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=STATUS, default='Nuevo')
    class Meta:
        model = Assignment
        fields = "__all__"

class UpdateAssignmentSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=STATUS, default='Nuevo')
    class Meta:
        model = Assignment
        fields = ["title", "description", 'status']

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        return instance

class UpdateAssignmentStatusSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=STATUS, default='Nuevo')
    class Meta:
        model = Assignment
        fields = ['status']

    def update(self, instance, validated_data):
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        return instance