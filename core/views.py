from django.views.generic import ListView, DetailView
#  ListView - Listar os posts criados
#  DetailView - mostrar os detalhes de um post

from .models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
