from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from accounts.models import UserProfile
from accounts.models import Profile, Address


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (name, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            self.fields[name].help_text = None

    phone = forms.CharField(required=True, max_length=10, min_length=10)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        exclude = ('username.help_text',)

        widgets = {
            'password': forms.PasswordInput(),
        }

    # def clean_username(self):
    #     username = self.cleaned_data.get('username',)

    def clean_email(self):
        email = self.cleaned_data.get('email', False)
        if not email:
            raise forms.ValidationError('Email is required')
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name', False)
        if not first_name:
            raise forms.ValidationError('First name is required')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name', False)
        if not last_name:
            raise forms.ValidationError('Last name is required')
        return last_name


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class PhoneForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = ('phone',)


class AddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Address
        exclude = ('profile', 'is_default',)
