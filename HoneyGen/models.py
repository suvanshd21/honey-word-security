from django.db import models

class user_credentials(models.Model):
	username = models.CharField(max_length = 20,primary_key=True)
	password = models.CharField(max_length = 400)
