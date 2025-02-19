from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trainers/', views.get_trainers, name='trainers-all'),
    path('trainer/<int:trainer_id>', views.get_one_trainer, name='trainer-one'),
]