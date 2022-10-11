from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.utils import timezone
from newsproj.models import *
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User, Group
from django import forms

class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.authorUser}'

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )


class BasicSignupForm(SignupForm):
    def save(self, request):
        User = super(BasicSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user


class New(models.Model):
    author_new = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Автор')
    category_new = models.ManyToManyField('Category', verbose_name = 'Категория')
    date_create = models.DateTimeField(default=timezone.now, verbose_name = 'Дата публикации')
    description = models.TextField(verbose_name = 'Текст')
    name = models.CharField(max_length=50, unique=True, verbose_name = 'Заголовок')

    def __str__(self):
        return f'{self.name}: {self.date_create}: {self.category_new}: {self.description}: {self.author_new}'

    def get_absolute_url(self):
        return f'/news/'

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    subscribers = models.ManyToManyField(User, max_length=100, through='SubscribeCategory', blank=True)

    def __str__(self):
        return self.name.title()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubscribeCategory(models.Model):
    subscribeUser = models.ForeignKey(User, on_delete=models.CASCADE)
    categoryUser = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subscribeUser}'

class NewCategory(models.Model):
    new = models.ForeignKey(New, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

