from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import NewsFilter
from datetime import datetime
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin


class NewsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    paginate_by = 4


class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/post.html'
    context_object_name = 'post'


class NewsSearch(ListView):
    model = Post
    ordering = ['title',]
    template_name = 'flatpages/search.html'
    context_object_name = 'search'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.utcnow()
        return context


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'flatpages/post_edit.html'


class PostEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'flatpages/post_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.change_post',)
    model = Post
    template_name = 'flatpages/post_delete.html'
    success_url = reverse_lazy('news')
