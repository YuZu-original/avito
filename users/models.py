from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

from users.utils import calculate_age


def check_birth_date(value: date):
    age = calculate_age(value)
    if age < 9:
        raise ValidationError('%(value)s is too small', params={'value': value})


class Location(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return self.name


class User(AbstractUser):
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLES = [
        (MEMBER, "Пользователь"),
        (MODERATOR, "Модератор"),
        (ADMIN, "Админ"),
    ]

    role = models.CharField(max_length=9, choices=ROLES, default=MEMBER)
    age = models.PositiveIntegerField(null=True)
    locations = models.ManyToManyField(Location)
    birth_date = models.DateField(validators=[check_birth_date], null=True)
    email = models.EmailField(unique=True, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
