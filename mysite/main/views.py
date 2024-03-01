from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db import transaction
from .models import Worker,Employment,Office,Profile
from .forms import WorkerForm, EmploymentForm, OfficeForm, WorkerDeleteForm, OfficeDeleteForm, ProfileEditForm, UserEditForm
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # Отримуємо всі офіси, які належать поточному користувачеві
    user_offices = Office.objects.filter(user=request.user)
    # Отримуємо всіх робітників, які працюють у цих офісах
    workers = Worker.objects.filter(offices__in=user_offices)
    return render(request, 'main/dashboard.html', {'workers': workers, 'section': 'dashboard'})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('dashboard')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'main/edit.html', {'user_form': user_form, 'profile_form': profile_form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('Logged in successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Account is invalid')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'main/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request, 'main/register.html', {'user_form': user_form})

def home(request):
    return render(request, 'main/f.html')

def sal(request):
    workers = Worker.objects.all()
    return render(request, 'main/salary.html', {'workers': workers})

@login_required
def add_work(request):
    form_error = None

    if request.method == 'POST':
        worker_form = WorkerForm(request.POST)
        employment_form = EmploymentForm(request.POST)

        if worker_form.is_valid() and employment_form.is_valid():
            try:
                with transaction.atomic():
                    worker = worker_form.save()
                    employment = employment_form.save(commit=False)
                    employment.worker = worker
                    employment.save()
                    worker.offices.set(Office.objects.filter(user=request.user))
            except Exception as e:
                form_error = f"Помилка при збереженні: {e}"
            else:
                return redirect('dashboard')
        else:
            form_error = 'Форма невірно заповнена'
    else:
        worker_form = WorkerForm()
        employment_form = EmploymentForm()

    return render(request, 'main/add_worker.html', {'worker_form': worker_form, 'employment_form': employment_form, 'form_error': form_error})

@login_required
def add_office(request):
    form_error = None

    if request.method == 'POST':
        office_form = OfficeForm(request.POST)
        if office_form.is_valid():
            try:
                office = office_form.save(commit=False)
                office.user = request.user  # Призначення поточного користувача до офісу
                office.save()
                return redirect('dashboard')
            except Exception as e:
                form_error = f"Помилка при збереженні офісу: {e}"
        else:
            form_error = 'Форма невірно заповнена'
    else:
        office_form = OfficeForm()

    return render(request, 'main/add_office.html', {'office_form': office_form, 'form_error': form_error})

def del_worker(request):
    workers = Worker.objects.all()
    form_error = None

    if request.method == 'POST':
        worker_form = WorkerDeleteForm(request.POST, workers=workers)
        if worker_form.is_valid():
            selected_worker = worker_form.cleaned_data['worker']
            try:
                with transaction.atomic():
                    selected_worker.delete()
            except Exception as e:
                form_error = f"Помилка при видаленні робітника: {e}"
        else:
            form_error = 'Форма невірно заповнена'
    else:
        worker_form = WorkerDeleteForm(workers=workers)

    return render(request, 'main/del_worker.html', {'worker_form': worker_form, 'form_error': form_error})

def deloffice(request):
    offices = Office.objects.all()
    form_error = None

    if request.method == 'POST':
        office_form = OfficeDeleteForm(request.POST, offices=offices)
        if office_form.is_valid():
            selected_office = office_form.cleaned_data['office']
            try:
                with transaction.atomic():
                    selected_office.delete()
            except Exception as e:
                form_error = f"Помилка при видаленні офісу: {e}"
        else:
            form_error = 'Форма невірно заповнена'
    else:
        office_form = OfficeDeleteForm(offices=offices)

    return render(request, 'main/del_office.html', {'office_form': office_form, 'form_error': form_error})