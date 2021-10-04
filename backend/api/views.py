from django.shortcuts import render
from .serializer import ProfileSerializer, ServiceSerializer, ReviewSerializer, UserSerializer
from .models import Profile, Review, Service
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import generics,status
from rest_framework import filters
# from rest_auth.registration.views import SocialLoginView


#user authentication
class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class UserViewSet(viewsets.ModelViewSet):
    """
    view or edit users.
    """
    # permission_classes = (IsAuthenticated,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)


# profile
class ProfileList(APIView):
    # permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializers = ProfileSerializer(profiles, many=True)
        return Response(serializers.data)


    def post(self, request, format=None):
        serializers = Profile(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

#single profile
class SingleProfile(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_project(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    
    def put(self, request, pk, format=None):
        profile= self.get_project(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_project(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# service
class ServiceList(APIView):
    # permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        services = Service.objects.all()
        serializers = ServiceSerializer(services, many=True)
        return Response(serializers.data)


    def post(self, request, format=None):
        serializers = Service(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)




# single service
class SingleService(APIView):
    permission_classes = (IsAuthenticated,)
    def get_project(self, pk):
        try:
            return Service.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        service = self.get_project(pk)
        serializers = ServiceSerializer(service)
        return Response(serializers.data)

    
    def put(self, request, pk, format=None):
        service= self.get_project(pk)
        serializers = ProfileSerializer(service, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        service = self.get_project(pk)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Review
class ReviewList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        reviews = Review.objects.all()
        serializers = ReviewSerializer(reviews, many=True)
        return Response(serializers.data)


    def post(self, request, format=None):
        serializers = Review(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# search user /service
class SearchServiceAPIView(generics.ListCreateAPIView):
    search_fields = ['service_title']
    filter_backends = (filters.SearchFilter,)
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class SearchUserAPIView(generics.ListCreateAPIView):
    search_fields = ['user']
    filter_backends = (filters.SearchFilter,)
    queryset = Profile.objects.all()
    serializer_class = ServiceSerializer