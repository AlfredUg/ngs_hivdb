from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('hivdb/home/', views.home, name='home'),
    path('hivdb/about/', views.about, name='about'),
    path('hivdb/login/', auth_views.LoginView.as_view(template_name='hivdb/login.html'),name='login'),
    path('hivdb/logout/', auth_views.LogoutView.as_view(template_name='hivdb/home.html')),
    
    path('hivdb/basic-search/', views.basic_search, name='basic_search'),
    path('hivdb/advanced-search/', views.advanced_search, name='advanced_search'),
    path('hivdb/participants-details/', views.retrieve_participants, name='participants'),
    path('hivdb/samples-details/', views.retrieve_samples, name='samples'),
    path('hivdb/consensus-sequences/', views.retrieve_sequences, name='sequences'),

    path('hivdb/uploads/', views.upload_multiple_files, name='uploads'),
    path('hivdb/upload-fastqs/', views.upload_fastqs, name='uploads_fastqs'),
    path('hivdb/upload-participants/', views.upload_participants, name='upload_participants'),
    path('hivdb/upload-samples/', views.upload_samples, name='upload_samples'),
    path('hivdb/upload-sequences/', views.upload_sequences, name='upload_sequences'),
    path('hivdb/upload-regimens/', views.upload_participant_regimen, name='upload_regimens'),
    path('hivdb/upload-success/', views.upload_success, name='success'),
    
    path('hivdb/ngs-data/', views.ngs_files, name='ngs'),

]