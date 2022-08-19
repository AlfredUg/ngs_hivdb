import pandas as pd
from hivdb.models import  *
        

def update_participant(df):
    for index, row in df.iterrows():
        participant.objects.update_or_create(
        name=row['name'],
        region=row['region'],
        age=row['age'],
        gender=row['gender'], 
        nationality=row['nationality'],
        religion=row['religion'], 
        employment=row['employment'], 
        tribe=row['tribe'], 
        education=row['education'], 
        maritalStatus=row['maritalStatus'], 
        district=row['district'],
        county=row['county']
        )
        
def update_sample(df):
    for index, row in df.iterrows():
        sample.objects.update_or_create(
        name=row['name'],
        specimen=row['specimen'],
        laboratory=row['laboratory'],
        labtech=row['labtech'], 
        volume=row['volume'],
        plasma=row['plasma'], 
        cd4=row['cd4'], 
        viralLoad=row['viralLoad'], 
        tube=row['tube'], 
        btebb=row['btebb'], 
        dopsep=row['dopsep'],
        )
    
def update_sequence(df):
    for index, row in df.iterrows():
        sequence.objects.update_or_create(
        accession=row['accession'],
        species=row['species'],
        date_created=row['date_created'],
        date_updated=row['date_updated'], 
        host=row['host'],
        gene=row['gene'], 
        length=row['length'], 
        subtype=row['subtype'], 
        sequencing_platform=row['sequencing_platform'], 
        )

def update_participant_regimen(df):
    for index, row in df.iterrows():
        participantRegimen.objects.update_or_create(
        participantID=row['participantID'],
        regimenID=row['regimenID'],
        start_date=row['start_date'],
        end_date=row['end_date'],
        )
