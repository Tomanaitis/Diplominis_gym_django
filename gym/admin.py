from django.contrib import admin

from .models import (Client, Membership, Payment, Schedule, TrainerSchedule, Trainer, TrainingSession, Reservation,
                     Profile, )


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
    list_display = ('name', 'max_capacity', 'description', 'schedule')
    list_editable = ('max_capacity', 'schedule')
    search_fields = ('name', 'description')


class TrainerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'specialization')
    list_editable = ('email', 'specialization')
    search_fields = ('specialization', 'last_name')
    inlines = [TrainerScheduleInline]


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    list_editable = ('email', 'phone_number')
    search_fields = ('last_name', 'email', 'phone_number')


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('week_day', 'start_date', 'start_time', 'end_date', 'end_time')
    list_editable = ('start_date', 'end_date', 'start_time', 'end_time')
    search_fields = ('week_day', 'start_date', 'end_date')


class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date', 'membership_type', 'membership_status', 'client')
    list_editable = ('name', 'start_date', 'end_date', 'membership_type', 'membership_status')


class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('client', 'rezervation_status')
    list_editable = ('rezervation_status',)

    # def get_training_session_name(self, obj):
    #     return obj.training_session.name
    # get_training_session_name.short_description = 'Training Session'


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('price', 'payment_date')
    list_editable = ('payment_date',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(TrainingSession, TrainingSessionAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Reservation, ReservationsAdmin)
admin.site.register(Profile)
