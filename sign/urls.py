from django.urls import path
from .views import UserProfileUpdate, upgrade_me

urlpatterns = [
    path('', include('allauth.urls')),
    path('<int:pk>/update', UserProfileUpdate.as_view(), name='account'),
    path('upgrade/', upgrade_me, name = 'upgrade')

]