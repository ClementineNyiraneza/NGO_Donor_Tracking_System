
import joblib
import os
from django.conf import settings
from .forms import PredictionForm
from django.shortcuts import render, redirect
from django.db.models import Q, Sum
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ProjectPhotoForm

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Donor, Project, Donation, Milestone
from .forms import DonorForm, ProjectForm, DonationForm, MilestoneForm, ProjectPhotoForm

def is_admin(user):
    return user.is_staff

def home(request):
    total_donors = Donor.objects.count()
    total_projects = Project.objects.count()
    total_donations = Donation.objects.count()
    total_funds = Donation.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    completed_milestones = Milestone.objects.filter(completed=True).count()
    pending_milestones = Milestone.objects.filter(completed=False).count()

    projects = Project.objects.all()

    project_names = []
    project_funds = []

    for project in projects:
        total = Donation.objects.filter(project=project).aggregate(
            Sum('amount')
        )['amount__sum'] or 0

        project_names.append(project.name)
        project_funds.append(float(total))

    context = {
        'total_donors': total_donors,
        'total_projects': total_projects,
        'total_donations': total_donations,
        'total_funds': total_funds,
        'completed_milestones': completed_milestones,
        'pending_milestones': pending_milestones,
        'project_names': project_names,
        'project_funds': project_funds,
    }

    return render(request, 'ngo/home.html', context)

def donor_list(request):
    query = request.GET.get('q')

    if query:
        donors = Donor.objects.filter(
            Q(name__icontains=query) | Q(country__icontains=query)
        )
    else:
        donors = Donor.objects.all()

    return render(request, 'ngo/donor_list.html', {'donors': donors, 'query': query})

def project_list(request):
    projects = Project.objects.all()

    for project in projects:
        project.total_raised = Donation.objects.filter(
            project=project
        ).aggregate(
            Sum('amount')
        )['amount__sum'] or 0

    return render(
        request,
        'ngo/project_list.html',
        {'projects': projects}
    )

@login_required
@user_passes_test(is_admin)
def donor_create(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donor_list')
    else:
        form = DonorForm()

    return render(request, 'ngo/donor_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def donor_update(request, pk):
    donor = Donor.objects.get(id=pk)

    if request.method == 'POST':
        form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('donor_list')
    else:
        form = DonorForm(instance=donor)

    return render(request, 'ngo/donor_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def donor_delete(request, pk):
    donor = Donor.objects.get(id=pk)

    if request.method == 'POST':
        donor.delete()
        return redirect('donor_list')

    return render(request, 'ngo/donor_confirm_delete.html', {'donor': donor})

@login_required
@user_passes_test(is_admin)
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()

    return render(request, 'ngo/project_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def project_update(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'ngo/project_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def project_delete(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('project_list')

    return render(request, 'ngo/project_confirm_delete.html', {'project': project})
def donation_list(request):
    donations = Donation.objects.all()
    return render(request, 'ngo/donation_list.html', {'donations': donations})

@login_required
@user_passes_test(is_admin)
def donation_create(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_list')
    else:
        form = DonationForm()

    return render(request, 'ngo/donation_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def donation_update(request, pk):
    donation = Donation.objects.get(id=pk)

    if request.method == 'POST':
        form = DonationForm(request.POST, instance=donation)
        if form.is_valid():
            form.save()
            return redirect('donation_list')
    else:
        form = DonationForm(instance=donation)

    return render(request, 'ngo/donation_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def donation_delete(request, pk):
    donation = Donation.objects.get(id=pk)

    if request.method == 'POST':
        donation.delete()
        return redirect('donation_list')

    return render(request, 'ngo/donation_confirm_delete.html', {'donation': donation})

def milestone_list(request):
    milestones = Milestone.objects.all()
    return render(request, 'ngo/milestone_list.html', {'milestones': milestones})

@login_required
@user_passes_test(is_admin)
def milestone_create(request):
    if request.method == 'POST':
        form = MilestoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('milestone_list')
    else:
        form = MilestoneForm()

    return render(request, 'ngo/milestone_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def milestone_update(request, pk):
    milestone = Milestone.objects.get(id=pk)

    if request.method == 'POST':
        form = MilestoneForm(request.POST, instance=milestone)
        if form.is_valid():
            form.save()
            return redirect('milestone_list')
    else:
        form = MilestoneForm(instance=milestone)

    return render(request, 'ngo/milestone_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def milestone_delete(request, pk):
    milestone = Milestone.objects.get(id=pk)

    if request.method == 'POST':
        milestone.delete()
        return redirect('milestone_list')

    return render(request, 'ngo/milestone_confirm_delete.html', {'milestone': milestone})

@login_required
@user_passes_test(is_admin)
def project_photo_upload(request):
    if request.method == 'POST':
        form = ProjectPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectPhotoForm()

    return render(request, 'ngo/project_photo_form.html', {'form': form})
@api_view(['GET'])
def project_total_donations_api(request, pk):
    total = Donation.objects.filter(project_id=pk).aggregate(Sum('amount'))['amount__sum'] or 0
    return Response({'project_id': pk, 'total_donations': total})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'ngo/register.html', {'form': form})
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(is_admin)
def project_photo_upload(request):
    if request.method == 'POST':
        form = ProjectPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectPhotoForm()

    return render(request, 'ngo/project_photo_form.html', {'form': form})
def predict_funding(request):
    prediction = None
    metrics = None

    metrics_path = os.path.join(
        settings.BASE_DIR,
        'ml_model',
        'model_metrics.pkl'
    )

    if os.path.exists(metrics_path):
        metrics = joblib.load(metrics_path)

    if request.method == 'POST':
        form = PredictionForm(request.POST)

        if form.is_valid():
            target_amount = form.cleaned_data['target_amount']
            number_of_donors = form.cleaned_data['number_of_donors']
            completed_milestones = form.cleaned_data['completed_milestones']
            pending_milestones = form.cleaned_data['pending_milestones']

            model_path = os.path.join(
                settings.BASE_DIR,
                'ml_model',
                'donation_model.pkl'
            )

            model = joblib.load(model_path)

            prediction = model.predict([[
                target_amount,
                number_of_donors,
                completed_milestones,
                pending_milestones
            ]])[0]

    else:
        form = PredictionForm()

    return render(
        request,
        'ngo/predict.html',
        {
            'form': form,
            'prediction': prediction,
            'metrics': metrics
        }
    )