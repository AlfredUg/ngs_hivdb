from django.shortcuts import render, redirect
from hivdb.models import  *
from django.http import HttpResponseRedirect
from hivdb.forms import *
from hivdb.uploads import *
import pandas as pd

from django.contrib.auth import login, authenticate, logout #add this
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib import messages
import os
from django.conf import settings
from pathlib import Path
import datetime
from django.contrib.auth.decorators import login_required



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

@login_required
def retrieve_participants(request):
    participants=participant.objects.all()
    context={
        'participants': participants
    }
    return render(request, "hivdb/participants.html", context)

@login_required
def retrieve_samples(request):
    samples=sample.objects.all()
    context={
        'samples': samples
    }
    return render(request, "hivdb/samples.html", context)

def retrieve_sequences(request):
    sequences=sequence.objects.all()
    context={
        'sequences': sequences
    }
    return render(request, "hivdb/consensus-sequences.html", context)

def advanced_search(request):
    context={'':''}
    return render(request, "hivdb/advanced-search.html", context)

@login_required
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

@login_required
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

@login_required
def upload_samples(request):
    samples_form = UploadSampleForm()
    if 'upload_sample_form' in request.POST:
            samples_form=UploadSampleForm(request.POST)
            samples_file=request.FILES['samples']
            if samples_form.is_valid():
                df=pd.read_csv(samples_file, delimiter=',')
                print(df)
                update_sample(df)
                return HttpResponseRedirect("/hivdb/upload-success/")                    
    
    context={
        'samples_form': samples_form,
    }
    return render(request, "hivdb/uploads-samples.html", context=context)


@login_required
def upload_sequences(request):
    sequences_form = UploadSequenceForm()
    if 'upload_sequence_form' in request.POST:
            sequences_form=UploadSequenceForm(request.POST)
            sequences_file=request.FILES['sequences']
            if sequences_form.is_valid():
                df=pd.read_csv(sequences_file, delimiter=',')
                print(df)
                update_sequence(df)
                return HttpResponseRedirect("/hivdb/upload-success/")                    
    
    context={
        'sequences_form': sequences_form,
    }
    return render(request, "hivdb/uploads-sequences.html", context=context)

@login_required
def upload_participant_regimen(request):
    participant_regimen_form = UploadParticipantRegimenForm()
    if 'upload_participant_regimen_form' in request.POST:
            participant_regimen_form=UploadParticipantRegimenForm(request.POST)
            participant_regimen_file=request.FILES['participantRegimen']
            if participant_regimen_form.is_valid():
                df=pd.read_csv(sequences_file, delimiter=',')
                print(df)
                update_participant_regimen(df)
                return HttpResponseRedirect("/hivdb/upload-success/")                    
    
    context={
        'participant_regimen_form': participant_regimen_form,
    }
    return render(request, "hivdb/uploads-regimen.html", context=context)

@login_required
def upload_success(request):
    return render(request, "hivdb/upload-success.html")

# from .models import UploadFastq
# fastqs = UploadFastq.objects()

@login_required
def ngs_files(request):

    path = os.path.join(settings.BASE_DIR, "Fastq")
    samples = []
    filesizes = []
    fullpaths = []
    filenames_ = []
    c_times = []
    m_times = []
    for f in os.listdir(path):
        if f.endswith("fastq") or f.endswith("fq"): # to avoid other files
            full_path_fastq_file = "%s/%s/%s" % (settings.BASE_DIR, "Fastq", f) # modify the concatenation to fit your neet
            file_size = round(os.path.getsize(full_path_fastq_file)/(1024 * 1024),2)
            sample_name = Path(full_path_fastq_file).stem
            c_time = os.path.getctime(full_path_fastq_file)
            c_time = datetime.datetime.fromtimestamp(c_time)
            m_time = os.path.getmtime(full_path_fastq_file)
            m_time = datetime.datetime.fromtimestamp(m_time)
            fullpaths.append(full_path_fastq_file)
            filesizes.append(file_size)
            samples.append(sample_name)
            filenames_.append(f)
            c_times.append(c_time)
            m_times.append(m_time)

    files_dict = {'sample':samples, 
                  'filename_': filenames_,
                  'fullpath':fullpaths, 
                  'filesize':filesizes,
                  'c_time':c_times, 
                  'm_time':m_times, 
                }
    
    files_df = pd.DataFrame(files_dict)
    print(files_df)
    context={'files_df': files_df}
    return render(request, "hivdb/ngs-data.html", context)


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

