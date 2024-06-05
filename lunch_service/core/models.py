from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    pass


class Restaurant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='menus',  on_delete=models.CASCADE)
    date = models.DateField()
    items = models.TextField()

    class Meta:
        unique_together = ('restaurant', 'date')

    def __str__(self):
        return f'{self.restaurant.name} - {self.date}'


class Vote(models.Model):
    employee = models.ForeignKey(Employee, related_name='votes', on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, related_name='votes', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('employee', 'date')