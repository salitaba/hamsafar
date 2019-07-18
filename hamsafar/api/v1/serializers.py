from django.contrib.auth.models import User
from hamsafar.models import Profile, Request
from rest_framework import serializers

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
    class Meta:
        model = Request
        fields = '__all__'
    def create(self, validated_data):
        return Request.objects.create(**validated_data)