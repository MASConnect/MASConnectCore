from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
import pytz


# Create your models here.


GENDERS = (
    ("M", "Male"),
    ("F", "Female")
)


class Address(models.Model):
    street_number = models.CharField(max_length=128)
    street1 = models.CharField(max_length=128)
    street2 = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=32)
    zip = models.IntegerField()

    # These two need to be changes to `PointField` as defined in the GeoDjango library
    latitude = models.CharField(max_length=128)
    longitude = models.CharField(max_length=128)

    def __str__(self):
        return " ".join([ self.street_number, self.street1, self.city, str(self.zip)])



class ContactInfo(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = PhoneNumberField(null=True, blank=True)


class Chapter(models.Model):
    name = models.CharField(max_length=128)
    logo = models.ImageField(null=True, blank=True)
    metro_area = models.CharField(max_length=32, null=True, blank=True)
    contact_info = models.OneToOneField(ContactInfo, null=True, blank=True, on_delete=models.SET_NULL)
    parent_chapter = models.ForeignKey("Chapter", null=True, blank=True,  on_delete=models.SET_NULL)

class User(AbstractUser):
    member_id = models.CharField(max_length=32, null=True, blank=True)
    phone = PhoneNumberField(blank=True, null=True)
    gender = models.CharField(max_length=16, choices=GENDERS, null=True, blank=True)
    birth_year = models.PositiveIntegerField(null=True, blank=True)
    member_status = models.BooleanField(null=True, blank=True)
    member_since = models.DateField(null=True, blank=True)
    timezone = models.CharField(choices=((tz, tz) for tz in pytz.all_timezones),
                                max_length=128, null=True, blank=True)
    address = models.OneToOneField(Address, null=True, blank=True, on_delete=models.SET_NULL)
    main_chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name


class Center(models.Model):
    name = models.CharField(max_length=256)
    chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True)
    address = models.OneToOneField(Address, null=True, blank=True, on_delete=models.SET_NULL)
    contact_info = models.OneToOneField(ContactInfo, null=True, blank=True, on_delete=models.SET_NULL)
    is_masjid = models.BooleanField(default=False)
    admins = models.ManyToManyField(User, related_name="centers")


class Event(models.Model):
    chapter = models.ManyToManyField(Chapter)
    center = models.ForeignKey(Center, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    location = models.ForeignKey(Address, null=True, blank=True, on_delete=models.SET_NULL)
    flyer = models.FileField(null=True, blank=True)
    contact_info = models.ManyToManyField(ContactInfo)
    social_media_link = models.URLField(blank=True, null=True)
    extra_info = models.TextField(null=True, blank=True)


class Channel(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    is_private = models.BooleanField(default=True)


class Message(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
