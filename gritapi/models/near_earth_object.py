from django.db import models
from django.contrib.auth.models import User

class NearEathObject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neo_reference = models.IntegerField()
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=250)
    estimated_diameter = models.IntegerField()
    is_potentially_hazardous = models.BooleanField()
    close_approach_date = models.DateField()
    miles_per_hour = models.CharField(max_length=50)
    orbiting_body =models.CharField(max_length=50)

