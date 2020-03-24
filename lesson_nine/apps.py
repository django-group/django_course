from django.apps import AppConfig


class LessonNineConfig(AppConfig):
    name = 'lesson_nine'

    def ready(self):
        import lesson_nine.signals