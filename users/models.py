from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        if not username:
            raise ValueError('Users must have an username')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self.create_user(email, username, first_name, last_name, password, **extra_fields)
        user.save(using=self._db)
        return user


# ВСЕГДА при создании ПОЛЬЗОВАТЕЛЬСКОЙ модели использовать AbstractBaseUser
class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, default='Yaroslav', verbose_name='First Name')
    last_name = models.CharField(max_length=50, default='Orlov', verbose_name='Last Name')
    username = models.CharField(max_length=20, unique=True, default='user', verbose_name='username')
    email = models.EmailField(unique=True, default='email@example.com', verbose_name='email address')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.id}, {self.username}, {self.email}"

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Customs Users'
