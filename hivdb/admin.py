from django.contrib import admin

# Register your models here.

from hivdb.models import *

admin.site.register(participant)

admin.site.register(sample)

admin.site.register(regimen)

admin.site.register(drug)

admin.site.register(sequence)
#admin.site.register(UploadFastq)