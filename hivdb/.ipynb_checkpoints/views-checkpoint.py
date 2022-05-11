from django.shortcuts import render, redirect
from hivdb.models import  *
from django.http import HttpResponseRedirect
from hivdb.forms import *
from hivdb.uploads import *
import pandas as pd

from django.contrib.auth import login, authenticate, logout #add this
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib import messages


# Create your views here.

#First, views for the static pages
def home(request):
    return render(request, 'hivdb/home.html')

def about(request):
    return render(request, 'hivdb/about-us.html')

def basic_search(request):
    participants=participant.objects.all()
    context={
        'participants': participants
    }
    return render(request, "hivdb/basic-search.html", context)

def advanced_search(request):
    context={'':''}
    return render(request, "hivdb/advanced-search.html", context)


def upload_fastqs(request):
    fastqs_form = UploadFileForm()    
    if request.method == 'POST':
        if 'upload_fastqs_form' in request.POST:
            fastqs_form = UploadFileForm(request.POST)
            files = request.FILES.getlist('fastqfiles')
            if fastqs_form.is_valid():
                for f in files:
                    file_instance = UploadFastq(fastqfiles=f)
                    file_instance.save()
                fastqs_form.save()
                return HttpResponseRedirect("/hivdb/upload-success/")
    context={
        'fastqs_form': fastqs_form,
    }
    
    return render(request, "hivdb/uploads-fastq.html", context=context)

def upload_participants(request):
    participants_form = UploadParticipantForm()
    if 'upload_participant_form' in request.POST:
            participants_form=UploadParticipantForm(request.POST)
            participants_file=request.FILES['participants']
            if participants_form.is_valid():
                df=pd.read_csv(participants_file, delimiter=',')
                print(df)
                update_participant(df)
                return HttpResponseRedirect("/hivdb/upload-success/")                    
    
    context={
        'participants_form': participants_form,
    }
    return render(request, "hivdb/uploads-participants.html", context=context)

def upload_samples(request):
    return render(request, "hivdb/uploads-samples.html")

def upload_sequences(request):
    return render(request, "hivdb/uploads-sequences.html")

def upload_regimens(request):
    return render(request, "hivdb/uploads-regimen.html")

def upload_success(request):
    return render(request, "hivdb/upload-success.html")


def upload_multiple_files(request):
    
    fastqs_form = UploadFileForm()
    participants_form = UploadParticipantForm()
    
    if request.method == 'POST':
        if 'upload_fastqs_form' in request.POST:
            fastqs_form = UploadFileForm(request.POST)
            files = request.FILES.getlist('fastqfiles')
            if fastqs_form.is_valid():
                for f in files:
                    file_instance = UploadFastq(fastqfiles=f)
                    file_instance.save()
                fastqs_form.save()
                return HttpResponseRedirect("/hivdb/upload-success/")
                
        elif 'upload_participant_form' in request.POST:
            participants_form=UploadParticipantForm(request.POST)
            participants_file=request.FILES['participants']
            if participants_form.is_valid():
                df=pd.read_csv(participants_file, delimiter=',')
                print(df)
                update_participant(df)
                return HttpResponseRedirect("/hivdb/upload-success/")                    
    
    context={
        'fastqs_form': fastqs_form,
        'participants_form': participants_form,
    }

    return render(request, "hivdb/uploads.html", context)

