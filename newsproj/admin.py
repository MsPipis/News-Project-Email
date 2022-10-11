from django.contrib import admin
from .models import Category, New, NewCategory, Author, SubscribeCategory
from django.contrib.auth.models import Group, User

admin.site.register(Category)
admin.site.register(New)
admin.site.register(NewCategory)
admin.site.register(Author)
admin.site.register(SubscribeCategory)