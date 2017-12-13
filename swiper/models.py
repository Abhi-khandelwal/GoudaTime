import uuid

from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import Storage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.
class Picture(models.Model):
    """
    Model to hold multiple pictures for a restaurant.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, help_text="Enter the picture name (e.g. Seating Area, or Kitchen)")
    image = models.ImageField(upload_to = 'swiper/static/img/', default = 'swiper/static/img/no-img.png')

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Restaurant(models.Model):
    """
    This model stores the required information pertaining to the restaurant
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=100, help_text="Enter the restaurant name (e.g. Santarpio's or Jimmy's Subs)")

    description = models.TextField(max_length=1000, help_text="Enter a brief description of the restaurant")
    address = models.CharField(max_length=75, help_text='123 Sample St, City ST 90210')

    hours = models.CharField(max_length=200, help_text="Enter the restaurant hours (e.g. M-F 9-5, Sat 12-5, Sun Closed)")
    pictures = models.ManyToManyField(Picture, help_text="Select pictures for this restaurant")

    category = models.CharField(max_length=50, help_text="Enter the general food category (e.g. Mexican, American, Thai, etc)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(self.name)

class MatchManager(models.Manager):
    """
    This is the manager class for the match system for creating users and helpful
    functions in general.
    """
    def total_matches():
        matches = Match.objects.all()
        return len(matches)

    def get_matches(user):
        matches = Match.objects.filter(user=user)
        return matches

    def check_match(user, restaurant):
        return Match.objects.filter(user=user, restaurant=restaurant)

    def add_match(user, restaurant):
        new_match = Match(user=user, restaurant=restaurant)
        new_match.save()

class Match(models.Model):
    """
    A match is a bi-directional association between a restaurant and user who
    wants the association (match).
    """
    user = models.ForeignKey(User, related_name="match_user")
    restaurant = models.ForeignKey(Restaurant, related_name="match_restaurant")
    date_matched = models.DateField(auto_now_add=True, editable=False)

class DenyManager(models.Manager):
    """
    This is the manager class for the deny system for creating denies and helpful
    functions in general for keeping track of denies.
    """
    def total_denies():
        denies = Deny.objects.all()
        return len(denies)

    def get_denies(user):
        denies = Deny.objects.filter(user=user)
        return denies

    def check_deny(user, restaurant):
        return Deny.objects.filter(user=user, restaurant=restaurant)

    def add_deny(user, restaurant):
        new_deny = Deny(user=user, restaurant=restaurant)
        new_deny.save()

class Deny(models.Model):
    """
    A deny is a bi-directional association between a restaurant and user who
    does not want the association (deny).
    """
    user = models.ForeignKey(User, related_name="deny_user")
    restaurant = models.ForeignKey(Restaurant, related_name="deny_restaurant")
    date_denied = models.DateField(auto_now_add=True, editable=False)
