from django.db import models
from django.contrib.auth.models import User

class schedule(models.Model):
	no_of_teams=models.IntegerField()
	duration=models.IntegerField()
class permutations(models.Model):
	team1=models.IntegerField()
	team2=models.IntegerField()
	winner_no=models.IntegerField()
	isallowed=models.BooleanField()
	
