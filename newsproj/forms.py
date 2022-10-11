from django import forms
from django.core.exceptions import ValidationError
from .models import New, Category, NewCategory, Author, SubscribeCategory
from django.forms import ModelForm
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group, User
from django.forms import ModelForm
from .models import BaseRegisterForm, BasicSignupForm

class NewForm(forms.ModelForm):
    description = forms.CharField(min_length=5)

    class Meta:
        model = New
        fields = '__all__'


    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("description")
        name = cleaned_data.get("name")
        author = cleaned_data.get("author")


        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

            return cleaned_data


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user


class SocialSignupForm(SignupForm):

    def save(self, request):
        user = super(SocialSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user


class UpdateProfileForm(ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff',
            'groups',
        ]

