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