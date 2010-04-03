from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

class SnippetManager(models.Manager):
    def top_authors(self):
        return User.objects.annotate(score=Count('snippet')).order_by('score')

class LanguageManager(models.Manager):
    def top_languages(self):
        return self.annotate(score=Count('snippet')).order_by('score')
