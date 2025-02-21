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
        ('W', 'Weekly'),
        ('M', 'Monthly'),
        ('Y', 'Yearly'),
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
    profile = models.ForeignKey(Profile, on_delete=SET_NULL, null=True, blank=True)
    description = HTMLField()

    def __str__(self):
        return f'{self.name} {self.start_date} {self.end_date} {self.membership_type}'


class Payment(models.Model):
    """
    Payments table class representing one payment
    """
    price = models.FloatField('Price', help_text='Enter payment price')
    payment_date = models.DateField('Payment_date', help_text="Enter date", default=date.today)
    membership = models.ForeignKey(Membership, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.price} EUR on {self.payment_date}'


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

    start_date = models.DateField('Start date', help_text="Enter date",
                                  default=date.today)
    end_date = models.DateField('End date', help_text="Enter date",
                                default=date.today)
    start_time = models.TimeField('Start time',
                                  help_text='Enter start time',
                                  default=get_current_time)

    end_time = models.TimeField('End time',
                                help_text='Enter End time',
                                default=get_current_time)

    def __str__(self):
        return f'{self.week_day} {self.start_date} {self.end_date}, {self.start_time} {self.end_time}'


class Trainer(models.Model):
    """
    Class representing trainers.
    """
    first_name = models.CharField('Name', max_length=50, help_text='Enter your name')
    last_name = models.CharField('Surname', max_length=50, help_text='Enter your surname')
    email = models.CharField('Email', max_length=50, help_text="Enter email adress")
    specialization = models.CharField('Specialization', max_length=100, default='Specialization....')
    professional_history = HTMLField()
    trainer_cover = models.ImageField('trainer_cover',
                                      upload_to='covers/trainer_covers',
                                      null=True,
                                      blank=True)
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
    schedule = models.ForeignKey(Schedule, on_delete=SET_NULL, null=True, blank=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='sessions')
    ts_cover = models.ImageField('training_session_cover',
                                 upload_to='covers/ts_covers',
                                 null=True,
                                 blank=True)

    def __str__(self):
        return f'{self.name}  {self.max_capacity}'


class TrainerSchedule(models.Model):
    """
    Class representing the trainer's schedule.
    """
    schedule = models.ForeignKey(Schedule, on_delete=SET_NULL, null=True, blank=True)
    trainer = models.ForeignKey(Trainer, on_delete=SET_NULL, null=True, blank=True)


class Reservation(models.Model):
    """
    Reservations table class representing one reservation
    """

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
    profile = models.ForeignKey(Profile, on_delete=SET_NULL, null=True, blank=True)
    training_session = models.ForeignKey(TrainingSession,
                                         on_delete=SET_NULL,
                                         null=True,
                                         blank=True,
                                         related_name='reservations')

    def __str__(self):
        return f'{self.rezervation_status}'
