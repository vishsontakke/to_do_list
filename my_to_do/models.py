from django.db import models

# Create your models here.
class Todolist(models.Model):
    title = models.CharField(max_length=256)
    discription = models.TextField()
    is_completed = models.BooleanField()

    def __str__(self) -> str:
        return self.title
