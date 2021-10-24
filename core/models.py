from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)  # Título do post
    slug = models.SlugField(max_length=255, unique=True) # Ex: Introdução Ao Python = introducao-ao-python (www.meublog.com/blog/introducao-ao-python)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #  ondelete=models.CASCADA gerará um efeito cascata que fará que o post seja deletado caso o autor seja deletado
    body = models.TextField()  # Corpo do post
    created = models.DateTimeField(auto_now_add=True)  # A data do post, auto_now_add=True adiciona automaticamente a data e hora que o post foi criado
    updated = models.DateTimeField(auto_now=True)  # Esse campo gravará a última data e hora que o post foi MODIFICADO.

    def __str__(self):
        return self.title