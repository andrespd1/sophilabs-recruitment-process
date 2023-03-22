from django.contrib import admin

from .models import Recruiter, Candidate, Interview

admin.site.register(Recruiter)
admin.site.register(Candidate)
admin.site.register(Interview)
