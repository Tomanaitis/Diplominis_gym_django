from django import forms

from .models import Profile, User, TrainingSessionReview


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture', 'phone_number')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class TrainingSessionReviewForm(forms.ModelForm):
    class Meta:
        model = TrainingSessionReview
        fields = ('content', 'training_session', 'reviewer')
        widgets = {
            'training_session': forms.HiddenInput(),
            'reviewer': forms.HiddenInput()

        }
