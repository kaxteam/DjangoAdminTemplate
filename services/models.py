from django.db import models

class SampleModel(models.Model):

    name = models.CharField(max_length=50)
