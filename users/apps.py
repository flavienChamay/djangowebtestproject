from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    #Activating our signals
    def ready(self):
        import users.signals
