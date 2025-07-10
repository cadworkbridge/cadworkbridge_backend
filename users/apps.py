from django.apps import AppConfig

class UsersConfig(AppConfig):
    """
    Configuration for the Accounts app.
    Sets the default field type for auto-generated fields and initializes app signals.
    """
    default_auto_field = 'django.db.models.BigAutoField'  # Ensure new models use BigAutoField by default
    name = 'users'

    def ready(self):
        """Initializes app-specific signals and other configurations."""
        from . import signals  # Avoid issues in certain import contexts


