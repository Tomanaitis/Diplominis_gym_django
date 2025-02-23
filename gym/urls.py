from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trainers/', views.get_trainers, name='trainers-all'),
    path('trainer/<int:trainer_id>', views.get_one_trainer, name='trainer-one'),
    path('displaymemberships/', views.DisplayMembershipListView.as_view(), name='displaymemberships-all'),
    path('displaymembership/<uuid:pk>', views.DisplayMembershipDetailView.as_view(), name='displaymembership-one'),
    path('search/', views.search, name='search'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.get_user_profile, name='user-profile'),
    path('trainingsessions/', views.TrainingSessionListView.as_view(), name='trainingsessions-all'),
    path('trainingsession/<int:pk>', views.TrainingSessionDetailView.as_view(), name='trainingsession-one'),
    path('reservations/', views.ReservarsionsListView.as_view(), name='reservations-all'),
    path('payment/', views.PaymentsListView.as_view(), name='payments-all'),
    path('menberships/', views.MembershipListView.as_view(), name='memberships-all'),
    path('memebership/<uuid:pk>', views.MembershipDetailView.as_view(), name='membership-one'),

]

