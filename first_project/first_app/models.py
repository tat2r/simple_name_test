from django.db import models

# Create your models here.


class PrimaryInfo(models.Model):
	name = models.CharField(max_length=256)
	email = models.EmailField()
	cell_phone = models.CharField(max_length=25)
	def __str__(self):
		return self.name