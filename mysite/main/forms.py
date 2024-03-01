from .models import Worker,Employment,Office
from django.forms import ModelForm, TextInput, DateInput, NumberInput, CheckboxSelectMultiple, ModelMultipleChoiceField
from django import forms
from django.contrib.auth.models import User
from django import forms
from .models import Worker, Profile


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
    widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
    widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class WorkerForm(forms.ModelForm):
    offices = ModelMultipleChoiceField(
        queryset=Office.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Worker
        fields = ['first_name', 'last_name', 'date_of_birth', 'offices']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': "Ім'я"}),
            'last_name': forms.TextInput(attrs={'placeholder': "Прізвище"}),
            'date_of_birth': forms.DateInput(attrs={'placeholder': "Дата народження"}),
        }
class EmploymentForm(ModelForm):
    class Meta:
        model = Employment
        fields = ['hire_date', 'position', 'salary']
        widgets = {
            'position': TextInput(attrs={'placeholder': "Посада"}),
            'hire_date': DateInput(attrs={'placeholder': "Дата прийняття на роботу"}),
        }


class OfficeForm(ModelForm):
    class Meta:
        model = Office
        fields = ['name', 'location']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': "Назва офісу"
            }),

            'location': TextInput(attrs={
                'placeholder': "Місце розташування"
            })
        }

class WorkerDeleteForm(forms.Form):
    worker = forms.ModelChoiceField(
        queryset=Worker.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'placeholder': 'Виберіть працівника'}),
    )

    def init(self, *args, **kwargs):
        workers = kwargs.pop('workers', None)
        super(WorkerDeleteForm, self).init(*args, **kwargs)

        if workers:
            self.fields['worker'].queryset = workers

class WorkerDeleteForm(forms.Form):
    worker = forms.ModelChoiceField(
        queryset=Worker.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'placeholder': 'Виберіть працівника'}),
    )

    def __init__(self, *args, **kwargs):
        workers = kwargs.pop('workers', None)
        super(WorkerDeleteForm, self).__init__(*args, **kwargs)

        if workers:
            self.fields['worker'].queryset = workers

class OfficeDeleteForm(forms.Form):
    office = forms.ModelChoiceField(
        queryset=Office.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'placeholder': 'Виберіть офіс'}),
    )

    def __init__(self, *args, **kwargs):
        offices = kwargs.pop('offices', None)
        super(OfficeDeleteForm, self).__init__(*args, **kwargs)

        if offices:
            self.fields['office'].queryset = offices