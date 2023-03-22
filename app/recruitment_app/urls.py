from django.urls import path, include
from . import views


urlpatterns = [
    path('recruiter/getRecruiter/', views.get_recruiter),
    path('recruiter/createRecruiter/', views.create_recruiter),
    path('candidate/createCandidate', views.create_candidate),
    path('candidate/getCandidate', views.get_candidate),
    path('interview/createInterview', views.create_interview),
]