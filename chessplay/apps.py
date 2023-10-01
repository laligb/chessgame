from django.apps import AppConfig


class ChessplayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chessplay'

    def ready(self):
        import chessplay.signals
