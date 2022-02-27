from django.db import models


class Thought(models.Model):
    pub_datetime = models.DateTimeField()
    moody = models.CharField(max_length=400, null=True)
    event = models.CharField(max_length=100, null=True)
    old_think = models.CharField(max_length=400, null=True)
    def __str__(self) -> str:
        return format(self.pub_datetime, '%Y%m%d%H%M%S') 

class NewThinking(models.Model):
    thought = models.ForeignKey(Thought, on_delete=models.CASCADE)
    new_think = models.CharField(max_length=400)

class FeelVariation(models.Model):
    feel = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.feel

class Feeling(models.Model):
    thought = models.ForeignKey(Thought, on_delete=models.CASCADE)
    feel_variation = models.ForeignKey(FeelVariation, on_delete=models.CASCADE)