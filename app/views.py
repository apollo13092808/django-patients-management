import imp
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Patient
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_control


# Create your views here.
def frontend(request):
    return render(request, 'frontend.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def backend(request):
    if 'q' in request.GET:
        q = request.GET['q']

        q_patients = Patient.objects.filter(
            Q(name__icontains=q) |
            Q(phone__icontains=q) |
            Q(email__icontains=q) |
            Q(age__icontains=q) |
            Q(gender__icontains=q) |
            Q(note__icontains=q)
        ).order_by('-created')
    else:
        q_patients = Patient.objects.all().order_by('-created')

    paginator = Paginator(q_patients, 5)
    page = request.GET.get('page')
    patients = paginator.get_page(page)

    context = {
        'patients': patients,
    }
    return render(request, 'backend.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def add_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        note = request.POST.get('note')
        if name and phone and email and age and gender or note:
            patient = Patient()
            patient.name = name
            patient.phone = phone
            patient.email = email
            patient.age = age
            patient.gender = gender
            patient.note = note
            patient.save()
            messages.success(request, "Patient added successfully.")
            return HttpResponseRedirect('/backend')
    else:
        return render(request, "add.html")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def patient(request, id):
    patient = Patient.objects.get(pk=id)
    context = {
        'patient': patient,
    }
    if patient is not None:
        return render(request, 'edit.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def edit_patient(request):
    if request.method == 'POST':
        patient = Patient.objects.get(id=request.POST.get('id'))
        if patient is not None:
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            patient.save()
            messages.success(request, "Patient updated successfully.")
            return HttpResponseRedirect('/backend')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def delete_patient(request, id):
    patient = Patient.objects.get(pk=id)
    patient.delete()
    messages.success(request, "Patient removed successfully.")
    return HttpResponseRedirect('/backend')
