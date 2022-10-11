import json
from django import template


register = template.Library()


CURRENCIES_SYMBOLS = {
   'rub': 'Р',
   'usd': '$',
}


@register.filter()
def currency(value, code='rub'):
   postfix = CURRENCIES_SYMBOLS[code]
   return f'{value} {postfix}'


@register.filter()
def censor(value):
   if isinstance(value, str):
      words = value.split()
      for word in words:
         if word == 'Редиска':
            value = value.replace("Редиска", "Р******")

   return f'{value}'


