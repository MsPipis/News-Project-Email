from django.urls import path, include
from django.contrib.flatpages import views
from django.contrib.auth.decorators import login_required
from .views import (
    NewsList, NewDetail, NewCreate, NewSearch, NewDelete, NewUpdate, ProfileUserUpdate, add_subscribe, delete_subscribe, BaseRegisterView, upgrade_me
)
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('', include('allauth.urls')),
    path('<int:pk>', NewDetail.as_view(), name='new_detail'),
    path('create/', NewCreate.as_view()),
    path('search/', NewSearch.as_view(), name='news_search'),
    path('<int:pk>/delete/', NewDelete.as_view()),
    path('<int:pk>/update/', NewUpdate.as_view()),
    path('upgrade/', upgrade_me, name = 'upgrade'),
    path('profile/<int:pk>/update/', ProfileUserUpdate.as_view(), name='profile_user_update'),
    path('add_subscribe/', add_subscribe, name='add_subscribe'),
    path('delete_subscribe/', delete_subscribe, name='delete_subscribe'),
]