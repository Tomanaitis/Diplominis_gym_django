from django.contrib import admin

from .models import Client, Membership, Payment, Schedule, TrainerSchedule, Trainer, TrainingSession, Reservation


class TrainerScheduleInline(admin.TabularInline):
    model = TrainerSchedule
    extra = 1


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
    list_display = ('week_day', 'start_date', 'end_date')
    list_editable = ('start_date', 'end_date')
    search_fields = ('week_day', 'start_date', 'end_date')


class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date', 'membership_type', 'membership_status', 'client')
    list_editable = ('name', 'start_date', 'end_date', 'membership_type', 'membership_status')


class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('client', 'rezervation_status', 'training_session')
    list_editable = ('rezervation_status',)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('price', 'payment_date')
    list_editable = ('payment_date',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(TrainingSession, TrainingSessionAdmin)
admin.site.register(TrainerSchedule)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Reservation, ReservationsAdmin)
