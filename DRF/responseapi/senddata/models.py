from django.db import models

class Data(models.Model):
	data1 = models.CharField(max_length=10)
	data2 = models.IntegerField()
	
	def __str__(self):
		return self.data1