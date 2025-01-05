from rest_framework import serializers
from .models import Task,Note

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields='__all__'

