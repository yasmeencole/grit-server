from django.db import models


class Favorite(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    neo = models.ForeignKey("NearEathObject", on_delete=models.CASCADE)
