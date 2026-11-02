from django.db import models
class Todo(models.Model):
    STATUS_CHOICES = [('Pending','Pending'),
                      ('In Progress','In Progress'),
                      ('Completed','Completed'),]
    task = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    status = models.CharField(max_length=20,choices= STATUS_CHOICES,default='Pending')
    def __str__(self):
        return self.task
    class Meta:
        db_table = 'todo'

