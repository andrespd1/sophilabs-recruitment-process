from rest_framework import serializers
from .models import Candidate, Recruiter, Interview


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = ('name', 'last_name')


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('name', 'last_name', 'applying_position', 'cv_link')


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = (
            'interview_type',
            'recruiter',
            'candidate',
            'appointment_date',
            'appointment_link',
            'notes'
        )


class InterviewCreateSerializer(serializers.Serializer):
    interview_type = serializers.IntegerField(required=True)
    appointment_date = serializers.DateTimeField(required=True)
    appointment_link = serializers.CharField(required=True)
