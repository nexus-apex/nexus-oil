import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Well, Production, OGEquipment


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['well_count'] = Well.objects.count()
    ctx['well_production'] = Well.objects.filter(well_type='production').count()
    ctx['well_injection'] = Well.objects.filter(well_type='injection').count()
    ctx['well_exploration'] = Well.objects.filter(well_type='exploration').count()
    ctx['well_total_depth_m'] = Well.objects.aggregate(t=Sum('depth_m'))['t'] or 0
    ctx['production_count'] = Production.objects.count()
    ctx['production_normal'] = Production.objects.filter(status='normal').count()
    ctx['production_low'] = Production.objects.filter(status='low').count()
    ctx['production_shutdown'] = Production.objects.filter(status='shutdown').count()
    ctx['production_total_oil_bbl'] = Production.objects.aggregate(t=Sum('oil_bbl'))['t'] or 0
    ctx['ogequipment_count'] = OGEquipment.objects.count()
    ctx['ogequipment_pump'] = OGEquipment.objects.filter(equipment_type='pump').count()
    ctx['ogequipment_compressor'] = OGEquipment.objects.filter(equipment_type='compressor').count()
    ctx['ogequipment_separator'] = OGEquipment.objects.filter(equipment_type='separator').count()
    ctx['recent'] = Well.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def well_list(request):
    qs = Well.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(well_type=status_filter)
    return render(request, 'well_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def well_create(request):
    if request.method == 'POST':
        obj = Well()
        obj.name = request.POST.get('name', '')
        obj.well_id = request.POST.get('well_id', '')
        obj.location = request.POST.get('location', '')
        obj.well_type = request.POST.get('well_type', '')
        obj.depth_m = request.POST.get('depth_m') or 0
        obj.status = request.POST.get('status', '')
        obj.daily_output = request.POST.get('daily_output') or 0
        obj.spud_date = request.POST.get('spud_date') or None
        obj.save()
        return redirect('/wells/')
    return render(request, 'well_form.html', {'editing': False})


@login_required
def well_edit(request, pk):
    obj = get_object_or_404(Well, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.well_id = request.POST.get('well_id', '')
        obj.location = request.POST.get('location', '')
        obj.well_type = request.POST.get('well_type', '')
        obj.depth_m = request.POST.get('depth_m') or 0
        obj.status = request.POST.get('status', '')
        obj.daily_output = request.POST.get('daily_output') or 0
        obj.spud_date = request.POST.get('spud_date') or None
        obj.save()
        return redirect('/wells/')
    return render(request, 'well_form.html', {'record': obj, 'editing': True})


@login_required
def well_delete(request, pk):
    obj = get_object_or_404(Well, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/wells/')


@login_required
def production_list(request):
    qs = Production.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(well_name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'production_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def production_create(request):
    if request.method == 'POST':
        obj = Production()
        obj.well_name = request.POST.get('well_name', '')
        obj.date = request.POST.get('date') or None
        obj.oil_bbl = request.POST.get('oil_bbl') or 0
        obj.gas_mcf = request.POST.get('gas_mcf') or 0
        obj.water_bbl = request.POST.get('water_bbl') or 0
        obj.uptime_hours = request.POST.get('uptime_hours') or 0
        obj.status = request.POST.get('status', '')
        obj.notes = request.POST.get('notes', '')
        obj.save()
        return redirect('/productions/')
    return render(request, 'production_form.html', {'editing': False})


@login_required
def production_edit(request, pk):
    obj = get_object_or_404(Production, pk=pk)
    if request.method == 'POST':
        obj.well_name = request.POST.get('well_name', '')
        obj.date = request.POST.get('date') or None
        obj.oil_bbl = request.POST.get('oil_bbl') or 0
        obj.gas_mcf = request.POST.get('gas_mcf') or 0
        obj.water_bbl = request.POST.get('water_bbl') or 0
        obj.uptime_hours = request.POST.get('uptime_hours') or 0
        obj.status = request.POST.get('status', '')
        obj.notes = request.POST.get('notes', '')
        obj.save()
        return redirect('/productions/')
    return render(request, 'production_form.html', {'record': obj, 'editing': True})


@login_required
def production_delete(request, pk):
    obj = get_object_or_404(Production, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/productions/')


@login_required
def ogequipment_list(request):
    qs = OGEquipment.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(equipment_type=status_filter)
    return render(request, 'ogequipment_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def ogequipment_create(request):
    if request.method == 'POST':
        obj = OGEquipment()
        obj.name = request.POST.get('name', '')
        obj.equipment_type = request.POST.get('equipment_type', '')
        obj.serial_number = request.POST.get('serial_number', '')
        obj.well_name = request.POST.get('well_name', '')
        obj.status = request.POST.get('status', '')
        obj.last_service = request.POST.get('last_service') or None
        obj.next_service = request.POST.get('next_service') or None
        obj.save()
        return redirect('/ogequipments/')
    return render(request, 'ogequipment_form.html', {'editing': False})


@login_required
def ogequipment_edit(request, pk):
    obj = get_object_or_404(OGEquipment, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.equipment_type = request.POST.get('equipment_type', '')
        obj.serial_number = request.POST.get('serial_number', '')
        obj.well_name = request.POST.get('well_name', '')
        obj.status = request.POST.get('status', '')
        obj.last_service = request.POST.get('last_service') or None
        obj.next_service = request.POST.get('next_service') or None
        obj.save()
        return redirect('/ogequipments/')
    return render(request, 'ogequipment_form.html', {'record': obj, 'editing': True})


@login_required
def ogequipment_delete(request, pk):
    obj = get_object_or_404(OGEquipment, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/ogequipments/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['well_count'] = Well.objects.count()
    data['production_count'] = Production.objects.count()
    data['ogequipment_count'] = OGEquipment.objects.count()
    return JsonResponse(data)
