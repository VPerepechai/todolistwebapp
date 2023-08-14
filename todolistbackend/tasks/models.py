import datetime

from django.db import models
from django.utils import timezone

class Task(models.Model):
    task_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    status_percentages = models.IntegerField(default=0)
    def __str__(self):
        return self.task_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Subtask(models.Model):
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    subtask_text = models.CharField(max_length=200)
    percentages = models.IntegerField(default=0)
    def __str__(self):
        return self.subtask_text