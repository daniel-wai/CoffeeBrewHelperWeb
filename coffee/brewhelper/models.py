from django.db import models

# Create your models here.
class brewstep(models.Model):
    step_id = models.IntegerField()
    change_in_water = models.IntegerField()
    change_in_time = models.IntegerField()

    def __str__(self):
        return f"Step {self.step_id}"