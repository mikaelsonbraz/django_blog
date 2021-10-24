from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "slug", "created", "updated")  #Mostrando o que exibir no cabeçalho dos Posts
    prepopulated_fields = {"slug": ("title",)}  #Fazendo com que o slug seja automaticamente preenchido enquanto preenche o titulo

