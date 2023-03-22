from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import RecruiterSerializer, CandidateSerializer, InterviewSerializer, InterviewCreateSerializer
from .models import Recruiter, Candidate, Interview
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import HttpResponse


@swagger_auto_schema(
    method='post',
    request_body=RecruiterSerializer,
    responses={201: RecruiterSerializer},
    operation_description="Creates a Recruiter"
)
@api_view(['POST'])
def create_recruiter(request):
    '''
    This function allows me to create a Recruiter for the interview process.
    '''
    serializer = RecruiterSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        return Response({
            'id': Recruiter(instance).__str__(),
            'data': serializer.data,
            'message': "The Recruiter has been created successfully"
        },
            status=201
        )


@swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="Id of the Recruiter", type=openapi.TYPE_STRING,
                          required=True),
    ],
    method='get',
    responses={
        200: RecruiterSerializer,
        404: "The Recruiter with the given Id wasn't found"
    },
    operation_description="Get a specific Recruiter with given an Id"
)
@api_view(['GET'])
def get_recruiter(request):
    '''
    This function allows to get a recruiter with a given id
    '''
    recruiter = get_object_or_404(Recruiter, id=request.GET.get('id'))
    serializer = RecruiterSerializer(recruiter)
    return Response({
        'data': serializer.data,
        'message': "The Recruiter has been found successfully"
    },
        status=200
    )


@swagger_auto_schema(
    operation_id='Candidate',
    method='post',
    request_body=CandidateSerializer,
    responses={201: CandidateSerializer},
    operation_description="Creates a Candidate"
)
@api_view(['POST'])
def create_candidate(request):
    '''
    This function allows to create a candidate for the interview process
    '''
    serializer = CandidateSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        return Response({
            'id': Candidate(instance).__str__(),
            'data': serializer.data,
            'message': "The Candidate has been created successfully"
        },
            status=201
        )


@swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter('id', openapi.IN_QUERY, description="Id of the Candidate", type=openapi.TYPE_STRING,
                          required=True),
    ],
    method='get',
    responses={
        200: CandidateSerializer,
        404: "The Candidate with the given Id wasn't found"
    },
    operation_description="Get a specific Candidate with given an Id"
)
@api_view(['GET'])
def get_candidate(request):
    '''
    This function allows to get a candidate with a given id
    '''
    candidate = get_object_or_404(Candidate, id=request.GET.get('id'))
    serializer = CandidateSerializer(candidate)
    return Response({
        'data': serializer.data,
        'message': "The Recruiter has been found successfully"
    },
        status=200
    )


@swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter('idRecruiter', openapi.IN_QUERY, description="Id of the Recruiter", type=openapi.TYPE_STRING,
                          required=True),
        openapi.Parameter('idCandidate', openapi.IN_QUERY, description="Id of the Candidate", type=openapi.TYPE_STRING,
                          required=True),
    ],
    method='post',
    request_body=InterviewSerializer,
    responses={201: InterviewSerializer},
    operation_description="Creates an Interview"
)
@api_view(['POST'])
def create_interview(request):
    '''
    This function uses a special Serializer to create an Interview,
    it requires that both recruiter and candidate has been created
    previously
    '''
    print()
    recruiter = get_object_or_404(Recruiter, id=request.GET.get('idRecruiter'))
    candidate = get_object_or_404(Candidate, id=request.GET.get('idCandidate'))
    if recruiter is not None and candidate is not None:
        serializer = InterviewSerializer(data=request.data)
        print(type(serializer))
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
