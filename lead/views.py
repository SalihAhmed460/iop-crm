from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render , redirect , get_object_or_404
from  .forms   import AddLeadForm
from .models import Lead
from client.models import Client
from team.models import Team

# Create your views here.
@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by = request.user)
    return render(request , 'lead/leads_list.html', {
        'leads': leads
    })
@login_required
def leads_detail(request, pk):
    lead = get_object_or_404(Lead, created_by = request.user ,pk=pk)

    lead = Lead.objects.filter(created_by = request.user).get(pk=pk)
    return render(request , 'lead/leads_detail.html',{
        'lead':lead
    })
@login_required
def leads_delete(request, pk):
    # Ensure the lead belongs to the logged-in user
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    # Only allow POST requests for deletion
    if request.method == 'POST':
        lead.delete()
        messages.success(request, 'Lead deleted successfully.')
        return redirect('leads:list')
    else:
        # Handle invalid request methods
        messages.error(request, 'Invalid request method.')
        return redirect('leads:list')
@login_required
def leads_edit(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    if request.method == 'POST':
        form = AddLeadForm(request.POST , instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lead edited successfully.')
            return redirect('leads:list')
    else:
        form = AddLeadForm(instance=lead)
        return render(request, 'lead/leads_edit.html', {
        'form': form,
        'lead': lead
    })

@login_required
def add_lead(request):
    team = Team.objects.filter(created_by=request.user)[0]
    if request.method == 'POST':  # Fix typo: ' POST' -> 'POST'
        form = AddLeadForm(request.POST)
        if form.is_valid():
            team = Team.objects.filter(created_by=request.user)[0]
            lead = form.save(commit=False)
            lead.created_by = request.user  # Assign the logged-in user
            lead.team = team
            lead.save()
            messages.success(request, 'Lead Added successfully.')
            return redirect('dashboard')  # Redirect to the dashboard
    else:
        form = AddLeadForm()

    return render(request, 'lead/add_lead.html', {
        'form': form,
        'team': team,
    })

@login_required 
def converted_to_client(request , pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    team = Team.objects.filter(created_by=request.user)[0]

    # Convert the lead to a client
    client = Client.objects.create(
        name=lead.name,
        email=lead.email,
        description=lead.description,
        created_by=request.user,
        team = team,
    )

    # Mark the lead as converted
    lead.converted = True
    lead.save()

    messages.success(request, 'Lead converted to client successfully.')
    return redirect('clients:list')