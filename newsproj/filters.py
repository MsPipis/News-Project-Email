import django.forms
import django_filters
from django.db import models
from django_filters import FilterSet, DateFilter, ModelChoiceFilter, NumberFilter
from .models import New, Category, NewCategory, Author
from django.forms import ModelForm
from django.forms.widgets import DateInput


class New_Filter(FilterSet):
    class Meta:
        model = New
        fields = ['name']


class Search_Filter(FilterSet):
    date_create = DateFilter(field_name='date_create',
                      lookup_expr='gt',
                      label='Дата',
                      widget=django.forms.DateInput(attrs={'type': 'date'}))
    date_create.field.error_messages = {'invalid': 'Enter date in format DD.MM.YYYY. Example: 31.12.2020'}
    date_create.field.widget.attrs = {'placeholder': 'DD.MM.YYYY'}
    author = ModelChoiceFilter(queryset=Author.objects.all(), field_name='Автор')


    class Meta:
        model = New
        fields = ['date_create', 'name', 'category_new', 'author_new']