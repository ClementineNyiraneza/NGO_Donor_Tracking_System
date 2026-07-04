

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),

    path('donors/', views.donor_list, name='donor_list'),
    path('donors/add/', views.donor_create, name='donor_create'),
    path('donors/edit/<int:pk>/', views.donor_update, name='donor_update'),
    path('donors/delete/<int:pk>/', views.donor_delete, name='donor_delete'),
    path('projects/add/', views.project_create, name='project_create'),
    path('projects/edit/<int:pk>/', views.project_update, name='project_update'),
    path('projects/delete/<int:pk>/', views.project_delete, name='project_delete'),
    path('projects/', views.project_list, name='project_list'),
    path('donations/', views.donation_list, name='donation_list'),
    path('donations/add/', views.donation_create, name='donation_create'),
    path('donations/edit/<int:pk>/', views.donation_update, name='donation_update'),
    path('donations/delete/<int:pk>/', views.donation_delete, name='donation_delete'),
    path('milestones/', views.milestone_list, name='milestone_list'),
    path('milestones/add/', views.milestone_create, name='milestone_create'),
    path('milestones/edit/<int:pk>/', views.milestone_update, name='milestone_update'),
    path('milestones/delete/<int:pk>/', views.milestone_delete, name='milestone_delete'),
    path('projects/photos/upload/', views.project_photo_upload, name='project_photo_upload'),
    path('api/projects/<int:pk>/total-donations/', views.project_total_donations_api, name='project_total_donations_api'),
    path('predict/', views.predict_funding, name='predict_funding'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='ngo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
path(
    'predict/',
    views.predict_funding,
    name='predict_funding'
),