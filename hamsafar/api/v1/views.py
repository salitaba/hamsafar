from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from hamsafar.models import Profile, RequestTravel
from hamsafar.api.v1.serializers import CreateProfileSerializer, ProfileSerializer, RequestSerializer, CreateRequestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ProfileView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = CreateProfileSerializer()

    def list(self, request):
        queryset = request.user.profile()
        serializer_class = ProfileSerializer(queryset,)
        return Response(serializer_class)


class RequestView(generics.ListCreateAPIView):
    queryset = RequestTravel.objects.all()
    serializer_class = RequestSerializer()

    def list(self, request):
        queryset = reuqest.user.requesttravel
        serializer_class = ReuqestSerializer(queryset,)
        return Response(serializer_class)


class ProfileAPIView(APIView):
    def get(self, request):
        profile = request.user.profile
        serializer = ProfileSerializer(profile,)
        response = {
            "profile": serializer.data
        }
        return Response(response)

    def post(self, request):
        profile = request.data.get('profile')
        serializer = CreateProfileSerializer(data=profile,)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({
            "response": 200
        })


class RequestAPIView(APIView):
    def get(self, request):
        permission_classes = [IsAuthenticated, ]
        user = request.user
        request_list = user.requesttravel_set.all()
        serializer = RequestSerializer(
            request_list,
            many=True
        )
        response = {
            'requests': serializer.data
        }
        return Response(response)
    def post(self, request):
        permission_classes = [IsAuthenticated,]
        user_id = request.user.id
        requset_travel = request.data.get('request')
        serializer = CreateRequestSerializer(
            data=requset_travel,
            context={'user_id': user_id}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({
            "response" : 200
        })

class FindNearAPIView(APIView):
    def get(self, request):
        permission_classes= [IsAuthenticated, ]
        request_list = RequestTravel.objects.all()
        serializer = RequestSerializer(request_list, many=True)
        response = {
            "requests": serializer.data
        }
        return Response(response)

    def post(self, request):
        permission_classes = [IsAuthenticated, ]
        requests = RequestTravel.objects.all()
        for request_travel in requests :
            request_travel.status = 'accepted'
            request_travel.save()
        return Response({
            "status": 200
        })
        