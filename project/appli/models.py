from django.db import models

# Create your models here.

class addproject(models.Model):
    name = models.CharField(max_length=200)
    descrption = models.TextField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20)
     

    def __str__(self):
        return self.name