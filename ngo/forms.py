from django import forms
#from .models import Donor, Project, Donation
from .models import Donor, Project, Donation, Milestone
from .models import Donor, Project, Donation, Milestone, ProjectPhoto

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'country', 'email']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'target_amount']

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['donor', 'project', 'amount', 'donation_date']
        widgets = {
            'donation_date': forms.DateInput(attrs={'type': 'date'})
        }
        
class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['project', 'title', 'completion_date', 'completed']
        widgets = {
            'completion_date': forms.DateInput(attrs={'type': 'date'})
        }


class ProjectPhotoForm(forms.ModelForm):
    class Meta:
        model = ProjectPhoto
        fields = ['project', 'image']




class PredictionForm(forms.Form):
    target_amount = forms.FloatField()
    number_of_donors = forms.IntegerField()
    completed_milestones = forms.IntegerField()
    pending_milestones = forms.IntegerField()