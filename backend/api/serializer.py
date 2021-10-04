from .models import Profile, Review, Service
from rest_framework import serializers
from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields =('id', 'username', 'email' , 'password')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True,'required':True}}

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user','profile_pic', 'gender', 'mobile','home_location', 'current_location' ,'bio','main_service', 'secondary_service_one', 'secondary_service_two' )


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'service_image','service_title', 'description' )


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','profile', 'service', 'task_description' 'review', 'rating', 'reviewed_by','reviewed_on' )


  