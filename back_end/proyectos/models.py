from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
