from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AppUser


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(required=True)
    height = forms.FloatField(required=True, label="Height (cm)", initial=180.0)

    class Meta:
        model = AppUser
        fields = ("username", "email", "password1", "password2", "height", "date_of_birth")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
