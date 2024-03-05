from django.db import models


class CourtManager(models.Manager):
    def available_courts(self):
        return self.filter(availabilityTag=True)


class Court(models.Model):
    courtID = models.AutoField(primary_key=True, default=0)
    title = models.CharField(max_length=100, null=True)
    availability = models.CharField(
        max_length=50, default="Available")
    num_availability = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    court_image = models.ImageField(
        upload_to='court_images/', blank=True, null=True)

    objects = CourtManager()

    def __str__(self):
        return self.title