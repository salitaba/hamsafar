from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from hamsafar.models import Profile, Request
from hamsafar.api.v1.serializers import CreateProfileSerializer, ProfileSerializer, RequestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
class ProfileView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = CreateProfileSerializer()

    def list(self, request):
        queryset = request.user.profile()
        serializer_class = ProfileSerializer(queryset,)
        return Response(serializer_class)

class RequestView(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer()

    def list(self, request):
        queryset = reuqest.user.request
        serializer_class = ReuqestSerializer(queryset,)
        return Response(serializer_class)

class ProfileAPIView(APIView):
    def get(self, request):
        profile = request.user.profile
        serializer = ProfileSerializer(profile,)
        response = {
            "profile" : serializer.data
        }
        return Response(response)
    def post(self, request):
        profile = request.data.get('profile')
        serializer = CreateProfileSerializer(data=profile,)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({
            "response" : "success"
        })

class RequestAPIView(APIView):
    def get(self, request):
        request = 