from django import forms
from django.forms import ClearableFileInput
from hivdb.models import *

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFastq
        fields = ['fastqfiles']
        widgets = {
            'fastqfiles': ClearableFileInput(attrs={'multiple': True}),
        }
        
    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['fastqfiles'].label = ""
        
class UploadParticipantForm(forms.Form):
    participants = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder':
        'Upload "participant.csv"', 'help_text': 'Choose a participant.csv file with participants to enter'}))
        
    def __init__(self, *args, **kwargs):
        super(UploadParticipantForm, self).__init__(*args, **kwargs)
        self.fields['participants'].label = ""
        
class UploadSampleForm(forms.Form):
    samples = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder':
        'Upload "sample.csv"', 'help_text': 'Choose a sample.csv file with samples to enter'}))
        
    def __init__(self, *args, **kwargs):
        super(UploadSampleForm, self).__init__(*args, **kwargs)
        self.fields['samples'].label = ""
        
class UploadSequenceForm(forms.Form):
    sequences = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder':
        'Upload "sequences.csv"', 'help_text': 'Choose a sequences.csv file with sequences to enter'}))
        
    def __init__(self, *args, **kwargs):
        super(UploadSequenceForm, self).__init__(*args, **kwargs)
        self.fields['sequences'].label = ""
        
class UploadParticipantRegimenForm(forms.Form): 
    participantRegimen = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder':
        'Upload "participantRegimen.csv"', 'help_text': 'Choose a participantRegimen.csv file with sequences to enter'}))
        
    def __init__(self, *args, **kwargs):
        super(UploadParticipantRegimenForm, self).__init__(*args, **kwargs)
        self.fields['participantRegimen'].label = ""
        