from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import TrainingSession, Membership, Trainer, DisplayMembership, Reservation, Payment, TrainingSessionReview
from .forms import ProfileUpdateForm, UserUpdateForm, TrainingSessionReviewForm
from .utils import check_password


def index(request):
    num_memberships = DisplayMembership.objects.count()
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
    paginator = Paginator(trainers, 4)
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


class DisplayMembershipListView(generic.ListView):
    model = DisplayMembership
    context_object_name = 'displaymembership_list'
    template_name = 'display_memberships.html'


class DisplayMembershipDetailView(generic.DetailView):
    model = DisplayMembership
    context_object_name = 'displaymembership'
    template_name = 'display_membership.html'


class TrainerListView(generic.ListView):
    model = Trainer
    context_object_name = 'trainer_list'
    template_name = 'trainers.html'
    paginate_by = 3


class TrainingSessionListView(generic.ListView):
    model = TrainingSession
    context_object_name = 'trainingsession_list'
    template_name = 'training_sessions.html'


class TrainingSessionDetailView(generic.edit.FormMixin, generic.DetailView):
    model = TrainingSession
    context_object_name = 'trainingsession'
    template_name = 'training_session.html'
    form_class = TrainingSessionReviewForm

    def post(self, request, *args, **kwargs):
        """
        skirta tik darbui su paciu post uzsklausa
        """
        form = self.get_form()  # TrainingSessionReviewForm instance
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        skirtas duomenu issaugojimui is views is formos gautu, validacijos metu mes irasom training sessiona ir useri
        """
        self.training_session_object = self.get_object()  #
        form.instance.training_session = self.training_session_object
        form.instance.reviewer = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        """
        were browser gonna go after successesful form post
        """
        return reverse('trainingsession-one', kwargs={'pk': self.training_session_object.id})


class ReservarsionsListView(generic.ListView):
    model = Reservation
    context_object_name = 'reservations'
    template_name = 'reservations.html'


class PaymentsListView(generic.ListView):
    model = Payment
    context_object_name = 'payments'
    template_name = 'payments.html'


def search(request):
    query_text = request.GET.get('search_text')
    search_results = Trainer.objects.filter(
        Q(last_name__icontains=query_text)
        | Q(specialization__icontains=query_text)
    )
    context = {'query_text': query_text,
               'trainer_list': search_results}
    return render(request, 'search_results.html', context=context)


@csrf_protect
def register_user(request):
    if request.method == 'GET':
        return render(request, 'registration/registration.html')
    elif request.method == 'POST':

        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not first_name or not last_name:
            messages.error(request, 'First name and Last name are required.')
            return redirect('register')

        if not check_password(password):
            messages.error(request, 'Password must be more than 5 symbols')
            return redirect('register')

        if password != password2:
            messages.error(request, 'Password missmatch')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, f'Vartotojo vardas {username} jau užimtas')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, f'Email {email} jau užregistruotas')
            return redirect('register')

        User.objects.create_user(username=username,
                                 email=email,
                                 password=password,
                                 first_name=first_name,
                                 last_name=last_name)

        messages.info(request, f'Vartotojas {username} užregistruotas!')
        return redirect('login')


@login_required()
@csrf_protect
def get_user_profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.info(request, "Your profile changes have been successfully saved.")
        else:
            messages.error(request, "Profile changes unsuccessful.")
        return redirect('user-profile')

    p_form = ProfileUpdateForm(instance=request.user.profile)
    u_form = UserUpdateForm(instance=request.user)

    context = {
        'p_form': p_form,
        'u_form': u_form
    }

    return render(request, 'profile.html', context=context)


class TrainingSessionReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = TrainingSessionReview
    template_name = 'staff_training_session_review_delete.html'
    context_object_name = 'trainingsessionreview'


    def get_success_url(self):
        trainingsessionreview_object = self.get_object()
        return reverse('trainingsession-one', kwargs={'pk': trainingsessionreview_object.training_session.id})

    def test_func(self):
        check = False
        for group in self.request.user.groups.all():
            if group.name == 'staff':
                check = True
        return check