from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
