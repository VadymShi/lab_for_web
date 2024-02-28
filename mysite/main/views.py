from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db import transaction
from .models import Worker,Employment,Office
from .forms import WorkerForm, EmploymentForm, OfficeForm, WorkerDeleteForm, OfficeDeleteForm
from django.views.generic import DetailView

def home(request):
    return render(request,'main/f.html')



def sal(request):
    workers = Worker.objects.all()
    return render(
        request,
        'main/salary.html',
        {'workers': workers},
    )
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
            except Exception as e:
                form_error = f"Помилка при збереженні: {e}"
            else:
                return redirect('home')
        else:
            form_error = 'Форма невірно заповнена'
    else:
        worker_form = WorkerForm()
        employment_form = EmploymentForm()

    return render(
        request,
        'main/add_worker.html',
        {
            'worker_form': worker_form,
            'employment_form': employment_form,
            'form_error': form_error,
        },
    )
def add_office(request):
    form_error = None

    if request.method == 'POST':
        office_form = OfficeForm(request.POST)

        if office_form.is_valid():
            try:
                office = office_form.save()
            except Exception as e:
                form_error = f"Помилка при збереженні офісу: {e}"
            else:
                return redirect('home')
        else:
            form_error = 'Форма невірно заповнена'

    else:
        office_form = OfficeForm()

    return render(
        request,
        'main/add_office.html',
        {
            'office_form': office_form,
            'form_error': form_error,
        },
    )
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

    return render(
        request,
        'main/del_worker.html',
        {
            'worker_form': worker_form,
            'form_error': form_error,
        },
    )

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

    return render(
        request,
        'main/del_office.html',
        {
            'office_form': office_form,
            'form_error': form_error,
        },
    )