from rest_framework import serializers
from .models import Employee, Restaurant, Menu, Vote


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = {'id', 'username', 'email', 'first_name', 'last_name'}


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = {'id', 'name'}


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = {'id', 'restaurant', 'date', 'item'}


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = {'id', 'employee', 'menu', 'date'}

