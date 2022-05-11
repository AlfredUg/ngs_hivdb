from django.db import models
from django.utils import timezone
import os

# Create your models here.    
class participant(models.Model):
    participant_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250, default="NA")
    region=models.CharField(max_length=250, default="NA")
    age=models.CharField(max_length=250, default="NA") 
    gender=models.CharField(max_length=250, default="NA")
    nationality=models.CharField(max_length=250, default="NA")
    religion=models.CharField(max_length=250, default="NA")
    employment=models.CharField(max_length=250, default="NA")
    tribe=models.CharField(max_length=250, default="NA")
    education=models.CharField(max_length=250, default="NA")
    maritalStatus=models.CharField(max_length=250, default="NA")
    district=models.CharField(max_length=250, default="NA")
    county=models.CharField(max_length=250, default="NA")

#we are using current date to hold this space, should change this when using real data
class sample(models.Model):
    sample_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50, default="NA")
    specimen=models.CharField(max_length=50, default="NA")
    laboratory=models.CharField(max_length=50, default="NA")
    labtech=models.CharField(max_length=250, default="NA")
    volume=models.IntegerField(default=0) 
    plasma=models.IntegerField(default=0) 
    cd4=models.IntegerField(default=0) 
    viralLoad=models.IntegerField(default=0) 
    tube=models.IntegerField(default=0) 
    btebb=models.DateField(default=timezone.now) 
    dopsep=models.DateField(default=timezone.now)

class sequence(models.Model):
    sequence_id=models.AutoField(primary_key=True)
    accession=models.CharField(max_length=50, default="NA")
    species=models.CharField(max_length=50, default="HIV")
    date_created=models.DateField(default=timezone.now) 
    date_updated=models.DateField(default=timezone.now)
    host=models.CharField(max_length=50, default="Human")
    gene=models.CharField(max_length=10, default="NA")
    subtype=models.CharField(max_length=10, default="NA")
    sequencing_platform=models.CharField(max_length=50, default="NA")
    residues=models.CharField(max_length=50, default="NA") #sequence/link to ngs file(s)
    
class drug(models.Model):
    drug_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50, default="NA")
    synonym=models.CharField(max_length=50, default="NA")
    abbreviation=models.CharField(max_length=50, default="NA")
    drugclass=models.CharField(max_length=250, default="NA")
    description=models.CharField(max_length=250, default="NA")
    
class regimen(models.Model):
    regimen_id=models.AutoField(primary_key=True)
    drug1=models.CharField(max_length=50, default="NA")
    drug2=models.CharField(max_length=50, default="NA")
    drug3=models.CharField(max_length=50, default="NA")
    abbreviation=models.CharField(max_length=10, default="NA")
    description=models.CharField(max_length=250, default="NA")
    treatmentLine=models.CharField(max_length=50, default="NA")
    
class participantSample(models.Model):
    participant_sample_id=models.AutoField(primary_key=True)
    participantID=models.ForeignKey(participant, on_delete=models.CASCADE, default=1)
    sampleID=models.ForeignKey(sample, on_delete=models.CASCADE, default=1)

class sampleSequence(models.Model):
    sample_sequence_id=models.AutoField(primary_key=True)
    sampleID=models.ForeignKey(sample, on_delete=models.CASCADE, default=1)
    sequenceID=models.ForeignKey(sequence, on_delete=models.CASCADE, default=1)
    
class participantRegimen(models.Model):
    participant_regimen_id=models.AutoField(primary_key=True)
    participantID=models.ForeignKey(participant, on_delete=models.CASCADE, default=1)
    regimenID=models.ForeignKey(regimen, on_delete=models.CASCADE, default=1)
    start_date=models.DateField(default=timezone.now) 
    end_date=models.DateField(default=timezone.now)

class project(models.Model):
    project_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250, default="NA")
    description=models.CharField(max_length=250, default="NA")
    
class UploadFastq(models.Model):
    #upload_folder = os.path.join('Fastq/', __str__(self.projectID))
    fastqfiles = models.FileField(upload_to='Fastq/', blank=True, null=True)