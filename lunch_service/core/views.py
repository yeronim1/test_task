from datetime import date
from django.db.models import Count
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Restaurant, Menu, Vote
from .serializers import RestaurantSerializer, MenuSerializer, VoteSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def today(self, request):
        today = date.today()
        menus = Menu.objects.filter(date=today)
        serializer = self.get_serializer(menus, many=True)
        return Response(serializer.data)


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def results(self, request):
        today = date.today()
        votes = Vote.objects.filter(date=today)
        results = votes.values('menu').annotate(count=Count('id')).order_by('-count')
        return Response(results)