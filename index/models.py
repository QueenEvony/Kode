from django.db import models

# Create your models here.

# I. Room number
# II. Amount paid 
# III. Occupant Name
# IV. Occupant Email
# V. Occupant Occupation
# VI. Number of night
# VII. Start date
# V. End Date

class Reservation (models.Model):
     name = models.CharField(max_length=10000)
     email = models.EmailField()
     occupation = models.CharField(max_length=10000, default="none")
     duration = models.IntegerField(default="0")
     date_started = models.DateField(auto_now_add=True)
     date_ended = models.DateField(auto_now_add=True)
     room_number = models.IntegerField(default="0")
     amount_paid = models.IntegerField(default="0")
