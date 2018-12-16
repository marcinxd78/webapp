from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class UrConfig(AppConfig):
    name = 'ur'
    verbose_name = 'Utrzymanie ruchu'




class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'