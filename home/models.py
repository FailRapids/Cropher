from django.db import models

class welcome(models.Model):
	header = models.CharField(max_length = 30,default = 'welcome')
	introduction = models.CharField(max_length=200)
	