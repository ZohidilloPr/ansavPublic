from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'id': 'email',
        'class': 'form-control',
        'placeholder': 'Emailni kiriting',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'password1',
        'class': 'form-control',
        'placeholder': 'passwordni kiriting',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'password2',
        'class': 'form-control',
        'placeholder': 'passwordni tasdiqlang',
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'id': 'username',
                'class': 'form-control',
                'placeholder': 'username',
            })
        }

    def save(self, commit=True):
        user = super(NewUserForm, self).save(
            commit=False)  # Call the real save() method
        user.email = self.cleaned_data['email']
        if commit:
           user.save()
        return user


class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(required=False, max_length=100)
    last_name = forms.CharField(required=False, max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

    def save(self, commit=True):
        user = super(UpdateUserForm, self).save(
            commit=False)  # Call the real save() method
        user.email = self.cleaned_data['email']
        if commit:
           user.save()
        return user


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image',)
