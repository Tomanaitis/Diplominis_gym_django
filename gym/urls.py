from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trainers/', views.get_trainers, name='trainers-all'),
    path('trainer/<int:trainer_id>', views.get_one_trainer, name='trainer-one'),
    path('memberships/', views.MembershipListView.as_view(), name='memberships-all'),
    path('memebership/<uuid:pk>', views.MembershipDetailView.as_view(), name='membership-one'),
    path('search/', views.search, name='search'),
]
