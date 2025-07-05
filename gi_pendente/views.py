from .forms import GiPendenteSemanaForm
from django.shortcuts import render, redirect
from .models import GiPendenteSemana

def gi_input_semana(request):
    if request.method == 'POST':
        form = GiPendenteSemanaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gi_dashboard')
    else:
        form = GiPendenteSemanaForm()
    return render(request, 'gi_pendente/gi_input_semana.html', {'form': form})

def gi_dashboard(request):
    semanas = GiPendenteSemana.objects.order_by('semana')
    labels = [str(s.semana) for s in semanas]
    data_realizado = [float(s.gi_realizado) for s in semanas]
    data_devido = [float(s.gi_devido) for s in semanas]
    return render(request, 'gi_pendente/gi_dashboard.html', {
        'semanas': semanas,
        'labels': labels,
        'data_realizado': data_realizado,
        'data_devido': data_devido,
    })