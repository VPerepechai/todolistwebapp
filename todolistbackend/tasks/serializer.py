from rest_framework import serializers
from .models import Task, Subtask


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ('subtask_text','percentages')

class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(source='subtask_set', many=True)

    class Meta:
        model = Task
        fields = ['id','subtasks','task_text','pub_date','status_percentages']
    
    def create(self, validated_data):
        print(validated_data)
        subtasks_data_list = validated_data.pop('subtask_set')
        task = Task.objects.create(**validated_data)
        for subtasks_data in subtasks_data_list:
            Subtask.objects.create(task=task, **subtasks_data)
        return task