from django.contrib import admin

from .models import (Membership, Payment, Schedule, Trainer, TrainingSession, Reservation,
                     Profile, DisplayMembership, TrainingSessionReview)


class ScheduleInline(admin.TabularInline):
    """
    Displays Schedule entries inline in the admin panel.
    """
    model = Schedule
    extra = 0


class ReservationsInline(admin.TabularInline):
    """
    Displays Reservation entries inline in the admin panel.
    """
    model = Reservation
    extra = 0


class PaymentInLine(admin.TabularInline):
    """
    Displays Payment entries inline in the admin panel.
    """
    model = Payment
    extra = 0


class TrainingSessionAdmin(admin.ModelAdmin):
    """
    Customizes the display of TrainingSession in the admin panel.
    """
    list_display = ('name', 'duration')
    search_fields = ('name', 'description')


class TrainerAdmin(admin.ModelAdmin):
    """
    Customizes the display of Trainer in the admin panel.
    Allows inline editing, search, displays related Schdedule inline.

    """
    list_display = ('first_name', 'last_name', 'email', 'specialization')
    list_editable = ('email', 'specialization')
    search_fields = ('specialization', 'last_name')
    inlines = [ScheduleInline]


class ScheduleAdmin(admin.ModelAdmin):
    """
    Configures the Schedule model display in the admin panel, allowing easy management of scheduling details,
    including inline editing, search functionality, and ordering of schedules by date and start time.
    """
    list_display = ('date', 'start_time', 'end_time', 'trainer', 'training_session', 'location', 'max_capacity')
    list_editable = ('start_time', 'end_time', 'trainer', 'training_session', 'location', 'max_capacity')
    search_fields = ('date', 'trainer')
    inlines = [ReservationsInline]
    ordering = ('date', 'start_time')


class MembershipAdmin(admin.ModelAdmin):
    """
    Configures the Membership model display in the admin panel.
    """
    list_display = ('id', 'user', 'name', 'start_date', 'end_date', 'membership_status')
    list_editable = ('start_date', 'end_date', 'name', 'membership_status')
    inlines = [PaymentInLine]


class ReservationsAdmin(admin.ModelAdmin):
    """
    Configures the Reservations model display in the admin panel.
    """
    list_display = ('user', 'rezervation_status', 'schedule')
    list_editable = ('rezervation_status', 'schedule')
    ordering = ('schedule', 'rezervation_status')


class ProfileAdmin(admin.ModelAdmin):
    """
    Configures the Profile model display in the admin panel.
    """
    list_display = ('user', 'phone_number')
    search_fields = ('user__username', 'phone_number')


class PaymentAdmin(admin.ModelAdmin):
    """
    Configures the Payment model display in the admin panel.
    """
    list_display = ('user', 'payment_date', 'membership', 'price', 'payment_status')
    list_editable = ('payment_date', 'membership', 'price', 'payment_status')
    ordering = ('payment_date', 'user')


class DisplayMembershipAdmin(admin.ModelAdmin):
    """
    Configures the DisplayMembership model display in the admin panel.
    """
    list_display = ('name', 'price')
    list_editable = ('price',)


admin.site.register(Membership, MembershipAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(TrainingSession, TrainingSessionAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Reservation, ReservationsAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(DisplayMembership, DisplayMembershipAdmin)
admin.site.register(TrainingSessionReview)
