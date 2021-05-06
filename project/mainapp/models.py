from django.db import models

class Stuff(models.Model):
    name = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вещь'
        verbose_name_plural = 'Вещи'
