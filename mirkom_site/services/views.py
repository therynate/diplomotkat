from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest, UsedDevice, PrebuiltPC
from .forms import SellForm, RepairForm, CustomPCForm


def home(request):
    return render(request, 'services/home.html')


@login_required
def sell(request):
    if request.method == 'POST':
        form = SellForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.user = request.user
            service.service_type = 'sell'
            service.save()
            return redirect('home')
    else:
        form = SellForm()
    return render(request, 'services/sell.html', {'form': form})


@login_required
def repair(request):
    if request.method == 'POST':
        form = RepairForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.user = request.user
            service.service_type = 'repair'
            service.save()
            return redirect('home')
    else:
        form = RepairForm()
    return render(request, 'services/repair.html', {'form': form})


def buy(request):
    devices = UsedDevice.objects.filter(is_available=True)
    return render(request, 'services/buy.html', {'devices': devices})


@login_required
def build_pc(request):
    if request.method == 'POST':
        form = CustomPCForm(request.POST)
        if form.is_valid():
            service = ServiceRequest(
                user=request.user,
                service_type='build_pc',
                description=form.cleaned_data['description'],
                title="Запрос на сборку ПК"
            )
            service.save()
            return redirect('home')
    else:
        form = CustomPCForm()

    prebuilt_pcs = PrebuiltPC.objects.filter(is_available=True)
    return render(request, 'services/build_pc.html', {
        'form': form,
        'prebuilt_pcs': prebuilt_pcs
    })