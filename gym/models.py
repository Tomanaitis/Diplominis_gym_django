from django.db import models
import uuid
import datetime
import PIL

from django.db.models import SET_NULL


class Client(models.Model):
    """
    class for clients table reprezenting one client
    """
    first_name = models.CharField('Name', max_length=50, help_text='Enter your name')
    last_name = models.CharField('Surname', max_length=50, help_text='Enter your surname')
    email = models.EmailField('Email', max_length=50, help_text="Enter email adress")
    phone_number = models.CharField('Phone_number', max_length=20, help_text='Enter your phone number')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.phone_number}'


class Membership(models.Model):
    """
    class for membership table reprezenting on membership
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField('Name', max_length=50)
    start_date = models.DateField('Start_date', max_length=15, help_text="Enter date",
                                  default=datetime.date.today)
    end_date = models.DateField('End_date', max_length=15, help_text="Enter date",
                                default=datetime.date.today)

    TYPE_STATUS = (
        ('W', 'Weekly'),
        ('q', 'Quarterly'),
        ('Y', 'Yearly'),
        ('t', 'Trial'),
    )
    membership_type = models.CharField('type',
                                       max_length=1,
                                       choices=TYPE_STATUS,
                                       default='t',
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
    client = models.ForeignKey(Client, on_delete=SET_NULL, null=True)

    def __str__(self):
        return f'{self.name} {self.start_date} {self.end_date} {self.membership_type}'


class Payment(models.Model):
    """
    Payments table class representing one payment
    """
    price = models.FloatField('Price', help_text='Enter payment price')
    payment_date = models.DateField('Payment_date', max_length=15, help_text="Enter date",
                                    default=datetime.date.today)
    membership = models.ForeignKey(Membership, on_delete=SET_NULL, null=True)

    def __str__(self):
        return f'{self.price}Eur {self.payment_date}'


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

    start_date = models.DateField('Start_date', max_length=15, help_text="Enter date",
                                  default=datetime.date.today)
    end_date = models.DateField('End_date', max_length=15, help_text="Enter date",
                                default=datetime.date.today)

    def __str__(self):
        return f'{self.week_day} {self.start_date} {self.end_date}'


class TrainingSession(models.Model):
    """
    Class respresents tables training session element
    """
    name = models.CharField('Name', max_length=50, help_text='Enter training sessions name')
    description = models.TextField('Description', max_length=2000, default='Sessions description...')
    max_capacity = models.PositiveIntegerField('Capacity', help_text="Enter max capacity")
    schedule = models.ForeignKey(Schedule, on_delete=SET_NULL, null=True)
    ts_cover = models.ImageField('training_session_cover',
                                 upload_to='covers/ts_covers',
                                 null=True,
                                 blank=True)

    def __str__(self):
        return f'{self.name} {self.description} {self.max_capacity}'


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
    client = models.ForeignKey(Client, on_delete=SET_NULL, null=True)
    training_session = models.ForeignKey(TrainingSession, on_delete=SET_NULL, null=True)

    def __str__(self):
        return f'{self.rezervation_status}'


class Trainer(models.Model):
    """
    Class representing trainers.
    """
    first_name = models.CharField('Name', max_length=50, help_text='Enter your name')
    last_name = models.CharField('Surname', max_length=50, help_text='Enter your surname')
    email = models.CharField('Email', max_length=50, help_text="Enter email adress")
    specialization = models.CharField('Specialization', max_length=100, default='Specialization....')
    professional_history = models.TextField('professional_history',
                                            max_length=2000,
                                            default='Professional accomplishments...'
                                            )
    trainer_cover = models.ImageField('trainer_cover',
                                      upload_to='covers/trainer_covers',
                                      null=True,
                                      blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.specialization}'

    class Meta:
        ordering = ('last_name', 'first_name')


class TrainerSchedule(models.Model):
    """
    Class representing the trainer's schedule.
    """
    schedule = models.ForeignKey(Schedule, on_delete=SET_NULL, null=True)
    trainer = models.ForeignKey(Trainer, on_delete=SET_NULL, null=True)
