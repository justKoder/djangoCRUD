from django.db import models

# Create your models here.


class Todo(models.Model):
    todo = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    scheduled = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return 'todo number ' + str(self.id)
