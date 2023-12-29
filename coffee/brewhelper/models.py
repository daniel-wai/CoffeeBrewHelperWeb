from django.db import models

# Create your models here.
class brewstep(models.Model):
    step_id = models.PositiveIntegerField()
    description = models.CharField(max_length=200, default='')
    change_in_water = models.IntegerField()
    change_in_time = models.IntegerField()

    def __str__(self):
        return f'Step {self.step_id}'

    class Meta:
        ordering = ['step_id']  # Choose a field for default ordering