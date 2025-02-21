from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from tinymce.models import HTMLField
from PIL import Image
import uuid

from django.db.models import SET_NULL


def get_current_time():
    return datetime.now().time()


class Profile(models.Model):
    """
    Class representig user profile
    """
    picture = models.ImageField(upload_to='profile_pics', default='default-user.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField('Phone Number',
                                    max_length=20,
                                    help_text='Enter your phone number',
                                    blank=True,
                                    null=True)

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.picture.path)
        thumb_size = (150, 150)
        img.thumbnail(thumb_size)
        img.save(self.picture.path)


class Membership(models.Model):
    """
    class for membership table reprezenting on membership
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField('Name', max_length=50)
    start_date = models.DateField('Start_date', help_text="Enter start date", default=date.today)
    end_date = models.DateField('End_date', help_text="Enter end date", default=date.today)

    TYPE_STATUS = (
        ('B', 'Basic'),
        ('F', 'Flexible'),
        ('P', 'Premium'),
        ('T', 'Trial'),
    )
    membership_type = models.CharField('type',
                                       max_length=1,
                                       choices=TYPE_STATUS,
                                       default='T',
                                       blank=True,
                                       help_text="Membership type"
                                       )

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
    # profile = models.ForeignKey(Profile, on_delete=SET_NULL, null=True, blank=True)
    description = HTMLField()

    def __str__(self):
        return f'{self.name} {self.start_date} - {self.end_date}'


class Payment(models.Model):
    """
    Payments table class representing one payment
    """
    price = models.FloatField('Price EUR', help_text='Enter payment price')
    payment_date = models.DateField('Payment_date', help_text="Enter date", default=date.today)
    membership = models.ForeignKey(Membership, on_delete=SET_NULL, null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=SET_NULL, null=True, blank=True)

    PAYMENT_STATUS = (
        ('p', 'Processing'),
        ('a', 'Active'),
        ('e', 'Expired'),
    )
    payment_status = models.CharField('status',
                                      max_length=1,
                                      choices=PAYMENT_STATUS,
                                      default='p',
                                      blank=True,
                                      help_text="Membership status"
                                      )

    def __str__(self):
        return f'{self.price} EUR on {self.payment_date} {self.membership} {self.profile}'


class Schedule(models.Model):
    """
    Class representing tables schedule
    """
    WEEK_DAY_STATUS = (
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday'),
    )
    week_day = models.CharField('Weekday',
                                max_length=1,
                                choices=WEEK_DAY_STATUS,
                                default='1',
                                blank=True,
                                help_text="Weekday"
                                )

    date = models.DateField('date', help_text="Enter date",
                            default=date.today)

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
        return f'{self.week_day} {self.date}, {self.start_time} {self.end_time} {self.location}'


class Trainer(models.Model):
    """
    Class representing trainers.
    """
    first_name = models.CharField('Name', max_length=50, help_text='Enter your name')
    last_name = models.CharField('Surname', max_length=50, help_text='Enter your surname')
    email = models.CharField('Email', max_length=50, help_text="Enter email adress")
    specialization = models.CharField('Specialization', max_length=100, default='Specialization....')
    professional_history = HTMLField()
    cover = models.ImageField(upload_to='covers/trainer_covers', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.specialization}'

    class Meta:
        ordering = ('last_name', 'first_name')


class TrainingSession(models.Model):
    """
    Class respresents tables training session element
    """
    name = models.CharField('Name', max_length=50, help_text='Enter training sessions name')
    description = HTMLField()
    max_capacity = models.PositiveIntegerField('Capacity', help_text="Enter max capacity")
    duration = models.DurationField(default="01:00:00", help_text="Default time is 1 hour")
    ts_cover = models.ImageField('training session cover',
                                 upload_to='covers/ts_covers',
                                 null=True,
                                 blank=True)

    def __str__(self):
        return f'{self.name}'


class TrainerSchedule(models.Model):
    """
    Class representing the trainer's schedule.
    """
    schedule = models.ForeignKey(Schedule, on_delete=SET_NULL, null=True, blank=True)
    trainer = models.ForeignKey(Trainer, on_delete=SET_NULL, null=True, blank=True)
    training_session = models.ForeignKey(TrainingSession, on_delete=SET_NULL, null=True, blank=True)


class Reservation(models.Model):
    """
    Reservations table class representing one reservation
    """
    profile = models.ForeignKey(Profile, on_delete=SET_NULL, null=True, blank=True)
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
    training_session = models.ForeignKey(TrainingSession,
                                         on_delete=SET_NULL,
                                         null=True,
                                         blank=True,
                                         related_name='reservations')

    def __str__(self):
        return f'{self.rezervation_status}'
