# from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


# class ShopConfig(AppConfig):
#     name = 'custom_admin'

# Параметр макета определяет, будет ли исходный стиль веб-страницы вертикальным или горизонтальным.
# Необязательный параметр - «горизонтальный» или «вертикальный»
# работает до версии Django 3.2?
class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
