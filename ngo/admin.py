from django.contrib import admin
from .models import Donor, Project, Donation, Milestone, ProjectPhoto

admin.site.register(Donor)
admin.site.register(Project)
admin.site.register(Donation)
admin.site.register(Milestone)
admin.site.register(ProjectPhoto)