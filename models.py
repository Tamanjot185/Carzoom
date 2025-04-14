from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Car(models.Model):  
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)
    features = models.TextField(blank=True)
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=100)

    def str(self):
        return f'{self.make} {self.model} ({self.year})'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.user.username} booked {self.car.make} from {self.start_time} to {self.end_time}'
