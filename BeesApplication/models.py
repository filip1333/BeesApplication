from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

USER_TYPE_CHOICES = [(1, 'Farmer'), (2, 'Beekeeper'), (3, 'Buyer')]


class User(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True)
    Role_name = USER_TYPE_CHOICES
    USERNAME_FIELD = 'identifier'
    role = models.CharField(choices=USER_TYPE_CHOICES, max_length=10)

    def _create_user(self, email, password, first_name, last_name, role):
        email = self.normalize_email(email)
        first_name = first_name.capitalize()
        last_name = last_name.capitalize()
        user = self.model(email=email, first_name=first_name, last_name=last_name, role=USER_TYPE_CHOICES)
        role = models.CharField(choices=USER_TYPE_CHOICES, max_length=10, required=True)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, role):
        return self._create_user(email, password, first_name, last_name, role)


class Role(models.Model):
    FARMER = 'F'
    BEEKEEPER = 'BE'
    BUYER = 'BU'
    USER_TYPE_CHOICES = [(FARMER, 'Farmer'), (BEEKEEPER, 'Beekeeper'), (BUYER, 'Buyer')]
    Role_name = models.CharField(choices=USER_TYPE_CHOICES, max_length=10, default=BUYER)
    department = models.CharField(max_length=100)

    class Meta:
        db_table = 'role'
