from django.db import models

class Preparation(models.Model):
    id = models.AutoField(primary_key=True)
    short = models.CharField(max_length=20)
    detail = models.CharField(max_length=600)

    def __str__(self):
        return self.short
