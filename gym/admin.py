from django.contrib import admin

from .models import (Membership, Payment, Schedule, TrainerSchedule, Trainer, TrainingSession, Reservation,
                     Profile)


class TrainerScheduleInline(admin.TabularInline):
    model = TrainerSchedule
    extra = 1


class ReservationsInline(admin.TabularInline):
    model = Reservation
    extra = 1


class TrainerScheduleAdmin(admin.ModelAdmin):
    list_display = ('trainer', 'schedule')
    inlines = [ReservationsInline]


class TrainingSessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'max_capacity')
    list_editable = ('duration', 'max_capacity',)
    search_fields = ('name', 'description')


class TrainerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'specialization')
    list_editable = ('email', 'specialization')
    search_fields = ('specialization', 'last_name')
    inlines = [TrainerScheduleInline]


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('date', 'start_time', 'end_time', 'trainer', 'training_session', 'location')
    list_editable = ('start_time', 'end_time', 'trainer', 'training_session', 'location')
    search_fields = ('date', 'trainer')


class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'membership_type', 'start_date', 'end_date', 'membership_status', 'profile')
    list_editable = ('start_date', 'end_date', 'membership_type', 'membership_status', 'profile')


class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('profile', 'rezervation_status', 'schedule')
    list_editable = ('rezervation_status', 'schedule')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')
    search_fields = ('user__username', 'phone_number')


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('profile', 'user', 'payment_date', 'membership', 'price', 'payment_status')
    list_editable = ('payment_date', 'membership', 'price', 'payment_status')


admin.site.register(Membership, MembershipAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(TrainingSession, TrainingSessionAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Reservation, ReservationsAdmin)
admin.site.register(Profile, ProfileAdmin)

