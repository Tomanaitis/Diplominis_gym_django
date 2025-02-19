from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse

from .models import TrainingSession, Membership, Trainer


def index(request):
    num_memberships = Membership.objects.count()
    num_trainers = Trainer.objects.count()
    num_training_sessions = TrainingSession.objects.count()

    context = {'num_trainers_t': num_trainers,
               'num_memberships_t': num_memberships,
               'num_training_sessions_t': num_training_sessions}

    return render(request, 'index.html', context=context)


def get_trainers(request):
    trainers = Trainer.objects.all()
    context = {'trainers': trainers}
    return render(request, 'trainers.html', context=context)


def get_one_trainer(request, trainer_id):
    one_trainer = get_object_or_404(Trainer, pk=trainer_id)
    context = {'one_trainer': one_trainer}
    return render(request, 'trainer.html', context=context)
