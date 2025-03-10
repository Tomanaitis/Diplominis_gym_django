from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from tinymce.models import HTMLField
from PIL import Image
import uuid

from django.db.models import SET_NULL


def get_current_time():
    """
    Returns the current time using the datetime module
    """
    return datetime.now().time()


class Profile(models.Model):
    """
    Class representig user profile.
    """

    picture = models.ImageField(upload_to='profile_pics', default='default-user.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField('Phone Number',
                                    max_length=20,
                                    help_text='Enter your phone number for news letters and notifications',
                                    blank=True,
                                    null=True)

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        """
        Represents a user profile, linked to a user account with a profile picture and optional phone number.
        """
        super().save(*args, **kwargs)
        img = Image.open(self.picture.path)
        thumb_size = (150, 150)
        img.thumbnail(thumb_size)
        img.save(self.picture.path)


class Membership(models.Model):
    """
    Represents a membership linked to a user.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField('Name', max_length=50, help_text="Trial, Basic, Flexible, Premium", default="Trial")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='membership')
    start_date = models.DateField('Start_date', help_text="Enter start date", default=date.today)
    end_date = models.DateField('End_date', help_text="Enter end date", default=date.today)

    STATUS_STATUS = (
        ('p', 'Processing'),
        ('a', 'Active'),
        ('e', 'Expired'),
    )
    membership_status = models.CharField('status',
                                         max_length=1,
                                         choices=STATUS_STATUS,
                                         default='p',
                                         blank=True,
                                         help_text="Membership status"
                                         )
    description = HTMLField(blank=True, default=None)

    def __str__(self):
        return f'{self.name} {self.start_date} - {self.end_date}'


class DisplayMembership(models.Model):
    """
    Represents a display version of membership.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField('Name', max_length=50)
    price = models.FloatField('Price EUR', help_text='Enter membership price')
    description = HTMLField()
    cover = models.ImageField(upload_to='covers/membership_covers', blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.price}'


class Payment(models.Model):
    """
    Represents a payment record linked to a user and an optional membership,
    tracking payment amount, date, and status, with an overdue check property.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    membership = models.ForeignKey(Membership, on_delete=SET_NULL, null=True, blank=True, related_name='payment')
    price = models.FloatField('Price EUR', help_text='Enter payment price')
    payment_date = models.DateField('Payment_date', help_text="Enter date", default=date.today)

    PAYMENT_STATUS = (
        ('p', 'Processing'),
        ('a', 'Paid'),
        ('e', 'Expired '),
    )
    payment_status = models.CharField('status',
                                      max_length=1,
                                      choices=PAYMENT_STATUS,
                                      default='p',
                                      blank=True,
                                      help_text="Membership status"
                                      )

    @property
    def is_overdue(self):
        """
        Checks if the payment is overdue by comparing the payment date with today's date
        """
        if self.payment_date and date.today() > self.payment_date:
            return True  # pradelsta
        else:
            return False

    def __str__(self):
        return f'{self.price} EUR on {self.payment_date} {self.membership}'


class Trainer(models.Model):
    """
    Represents a trainer with personal details.
    """
    first_name = models.CharField('Name', max_length=50, help_text='Enter your name')
    last_name = models.CharField('Surname', max_length=50, help_text='Enter your surname')
    email = models.CharField('Email', max_length=50, help_text="Enter email adress")
    specialization = models.CharField('Specialization', max_length=100, default='Specialization....')
    professional_history = HTMLField()
    cover = models.ImageField(upload_to='covers/trainer_covers', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ('last_name', 'first_name')


class TrainingSession(models.Model):
    """
    Represents a training session.
    """
    name = models.CharField('Name', max_length=50, help_text='Enter training sessions name')
    duration = models.DurationField(default="01:00:00", help_text="Default time is 1 hour")
    description = HTMLField()
    ts_cover = models.ImageField('training session cover',
                                 upload_to='covers/ts_covers',
                                 null=True,
                                 blank=True)

    def __str__(self):
        return f'{self.name}'


class Schedule(models.Model):
    """
    Represents a schedule for training sessions, including date, time,
    trainer, location, and maximum capacity, helping to organize gym classes.
    """
    max_capacity = models.PositiveIntegerField('Capacity', null=True, blank=True,
                                               help_text="Enter max capacity")
    date = models.DateField('date', help_text="Enter date", default=date.today)
    trainer = models.ForeignKey(Trainer, on_delete=SET_NULL, null=True, blank=True)
    training_session = models.ForeignKey(TrainingSession, on_delete=SET_NULL,
                                         null=True, blank=True, related_name='schedule')
    start_time = models.TimeField('Start time',
                                  help_text='Enter start time',
                                  default=get_current_time)
    end_time = models.TimeField('End time',
                                help_text='Enter End time',
                                default=get_current_time)

    LOCATION_NAME = (
        ('1', 'Main Studio'),
        ('2', 'Yoga Room'),
        ('3', 'Cardio Zone'),
        ('4', 'Outdoor Terrace'),
        ('5', 'Functional Training Area'),
    )
    location = models.CharField('Location',
                                max_length=1,
                                choices=LOCATION_NAME,
                                default='1',
                                blank=True,
                                help_text="Gym class locations"
                                )

    def __str__(self):
        return f'{self.date}, {self.start_time} {self.end_time} {self.training_session}'


class Reservation(models.Model):
    """
    Reservations table class representing one reservation
    """

    schedule = models.ForeignKey(Schedule, on_delete=SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    RESERVATION_STATUS = (
        ('p', 'Processing'),
        ('r', 'Reserved'),
        ('e', 'Unavailable'),
    )
    rezervation_status = models.CharField('rezervation_status',
                                          max_length=1,
                                          choices=RESERVATION_STATUS,
                                          default='p',
                                          blank=True,
                                          help_text="Membership status"
                                          )

    def __str__(self):
        return f'{self.rezervation_status}'


class TrainingSessionReview(models.Model):
    """
    Represents user reviews for training sessions.
    """
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField('Review', max_length=2000)
    training_session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE, blank=True)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.date_created}, {self.reviewer}, {self.training_session} {self.content[:50]}'
