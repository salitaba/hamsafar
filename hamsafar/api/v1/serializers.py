from django.contrib.auth.models import User
from hamsafar.models import Profile, RequestTravel
from rest_framework import serializers

import json
import requests
# import request
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )
    

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = '__all__'
    
class CreateProfileSerializer(serializers.ModelSerializer):
    user = CreateUserSerializer()
    class Meta:
        model = Profile
        fields = '__all__'
    def create(self, validated_data):
        user_detail = validated_data.pop('user')
        password = user_detail['password']
        user = User.objects.create_user(username=user_detail['username'], password=password)
        user.save()
        validated_data['user'] = user

        profile = Profile(**validated_data)
        profile.save()
        return profile


class RequestSerializer(serializers.ModelSerializer): 
    user = UserSerializer()
    class Meta:
        model = RequestTravel
        fields = '__all__'
    
class CreateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestTravel
        fields = ('start_lat', 'start_long','end_lat', 'end_long', 'status')
    def create(self, validated_data):
        user_id = self.context.get("user_id")
        print(type(user_id))
        validated_data['user'] = User.objects.get(id=user_id)


        url = "https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={}&lon={}".format(validated_data['start_lat'], validated_data['start_long'])
        # print(url)
        req = requests.get(url)
        data = json.loads(req.content.decode('utf-8'))
        validated_data['start_road'] = data['address']['road']

        url = "https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={}&lon={}".format(validated_data['end_lat'], validated_data['end_long'])
        req = requests.get(url)
        data = json.loads(req.content.decode('utf-8'))
        validated_data['end_road'] = data['address']['road'] 

        return RequestTravel.objects.create(**validated_data)