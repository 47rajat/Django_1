from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dreamreal(models.Model):
	""" model class represents a table or a collection in our DB"""
	website  = models.CharField(max_length = 50)
	mail = models.CharField(max_length = 50)
	name = models.CharField(max_length = 50)
	phonenumber = models.IntegerField()
	online = models.ForeignKey('Online', default = 1)

	class Meta:
		db_table = "dreamreal"

class Online(models.Model):
	domain = models.CharField(max_length = 30)
	class Meta:
		db_table = "online"

			