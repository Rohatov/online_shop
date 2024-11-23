from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('The Phone field must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=50, unique=True)
    USERNAME_FIELD = 'phone'
    photo = models.ImageField(upload_to='profile/', default='profile.profile.svg')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(
    Group,
    verbose_name=('groups'),
    blank=True,
    help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
    related_name='customuser_set'
    )

    user_permissions = models.ManyToManyField(
    Permission,
    verbose_name=('user permissions'),
    blank=True,
    help_text=('Specific permissions for this user.'),
    related_name='customuser_set'
)



    objects = MyUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = [] 

    @property
    def full_name(self):
        return f'{self.first_name} - {self.last_name}'
    
