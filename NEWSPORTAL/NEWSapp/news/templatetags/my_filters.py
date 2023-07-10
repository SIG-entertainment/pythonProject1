from django import template


register = template.Library()

@register.filter()
def postTime(dateCraetion):
   """
   value: значение, к которому нужно применить фильтр
   code: код валюты
   """

   # Возвращаемое функцией значение подставится в шаблон.
   return f'{dateCraetion}'
