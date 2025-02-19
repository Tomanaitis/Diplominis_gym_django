from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Q
from django.core.paginator import Paginator

from .models import TrainingSession, Membership, Trainer


def index(request):
    num_memberships = Membership.objects.count()
    num_trainers = Trainer.objects.count()
    num_training_sessions = TrainingSession.objects.count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
                'num_trainers_t': num_trainers,
                'num_memberships_t': num_memberships,
                'num_training_sessions_t': num_training_sessions,
                'num_visits_t': num_visits
               }

    return render(request, 'index.html', context=context)


def get_trainers(request):
    trainers = Trainer.objects.all()
    paginator = Paginator(trainers, 1)
    page_number = request.GET.get('page')
    paged_trainers = paginator.get_page(page_number)
    context = {'trainers': paged_trainers}
    return render(request, 'trainers.html', context=context)


def get_one_trainer(request, trainer_id):
    one_trainer = get_object_or_404(Trainer, pk=trainer_id)
    context = {'one_trainer': one_trainer}
    return render(request, 'trainer.html', context=context)


class MembershipListView(generic.ListView):
    model = Membership
    context_object_name = 'membership_list'
    template_name = 'memberships.html'

class MembershipDetailView(generic.DetailView):
    model = Membership
    context_object_name = 'membership'
    template_name = 'membership.html'

class TrainerListView(generic.ListView):
    model = Trainer
    context_object_name = 'trainer_list'
    template_name = 'trainers.html'
    paginate_by = 1


def search(request):
    query_text = request.GET.get('search_text')
    search_results = Trainer.objects.filter(
        Q(last_name__icontains=query_text)
        | Q(specialization__icontains=query_text)
    )
    context = {'query_text': query_text,
               'trainer_list': search_results}
    return render(request, 'search_results.html', context=context)

