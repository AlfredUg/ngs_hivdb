from django.contrib import admin

# Register your models here.

from hivdb.models import *

admin.site.register(participant)

admin.site.register(sample)

#admin.site.register(UploadFastq)