from django.contrib.auth.models import AbstractUser
from django.db import models


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

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
