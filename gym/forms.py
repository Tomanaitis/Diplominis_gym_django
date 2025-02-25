from django import forms

from .models import Profile, User, TrainingSessionReview


class ProfileUpdateForm(forms.ModelForm):
    """
    Form for updating user profile information, specifically phone number and profile picture.
    """
    class Meta:
        model = Profile
        fields = ('phone_number', 'picture')


class UserUpdateForm(forms.ModelForm):
    """
    Form for updating user account details, including first name, last name, and email.
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class TrainingSessionReviewForm(forms.ModelForm):
    """
    Form for submitting reviews for training sessions, with hidden fields for
    training session and reviewer to ensure they are not editable by the user.
    """
    class Meta:
        model = TrainingSessionReview
        fields = ('content', 'training_session', 'reviewer')
        widgets = {
            'training_session': forms.HiddenInput(),
            'reviewer': forms.HiddenInput()

        }
