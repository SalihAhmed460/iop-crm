from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import ClientForm
from team.models import Team
@login_required
def clients_list(request):
    clients = Client.objects.filter(created_by=request.user)
    return render(request, 'clients/clients_list.html', {'clients': clients})

@login_required
def clients_detail(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    return render(request, 'clients/clients_detail.html', {'client': client})

@login_required
def clients_add(request):
    team = Team.objects.filter(created_by=request.user)[0]
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            team = Team.objects.filter(created_by=request.user)[0]
            client = form.save(commit=False)
            client.created_by = request.user
            client.team = team
            client.save()
            return redirect('clients:list')
    else:
        form = ClientForm()
    return render(request, 'clients/clients_add.html', {
        'form': form,
        'team':team
        })

@login_required
def clients_edit(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients:list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/clients_edit.html', {'form': form, 'client': client})

@login_required
def clients_delete(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('clients:list')
    return render(request, 'clients/clients_delete.html', {'client': client})