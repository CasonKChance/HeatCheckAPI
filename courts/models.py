from django.db import models


class Court(models.Model):
    courtID = models.AutoField(primary_key=True)
    num_availability = models.PositiveIntegerField()
    availabilityTag = models.BooleanField(default=True)
    address = models.CharField(max_length=255)
    court_image = models.ImageField(
        upload_to='court_images/', blank=True, null=True)

    def __str__(self):
        return self.address
