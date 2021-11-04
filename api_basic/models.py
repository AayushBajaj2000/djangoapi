from django.db import models

# State model which indicates if the light is on or off
class State(models.Model):
    light_1 = models.CharField(max_length=50)

    def __str__(self):
        return self.light_1
