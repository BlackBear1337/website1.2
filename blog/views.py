from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from blog.models import Post, Comment


class PostList(ListView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_list.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        queryset = self.get_queryset()
        paginator = self.get_paginator(self.get_queryset(), self.get_paginate_by(queryset))
        page = int(self.request.GET.get('page', 1))
        start = page - 1 if page - 1 > 0 else 1
        context['page_range'] = paginator.page_range[start:page + 3]
        return context


class AdminPanelView(ListView):

    def get(self, request):
        post = Post.objects.all()
        return render(request, 'blog/admin_list.html', {'post': post})


class PostCreate(CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    extra_context = {'title': 'Create post'}
    context_object_name = 'form'
    fields = {'title', 'content', 'draft', 'category', 'author', 'tags', 'avatar'}


class EditView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = {'title', 'content', 'tags', 'category', 'avatar'}
    template_name_suffix = 'post_edit'


class PostDetails(DetailView):
    model = Post
    template_name = 'blog/post_details.html'
    context_object_name = 'post'


class PostDelete(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    extra_context = {'title': 'Delete Post'}
    success_url = '/'


class PostComment(CreateView):
    model = Comment
    extra_context = {'title': 'Comment'}
    context_object_name = 'comment'
    template_name = 'blog/post_comment.html'
    fields = {'text', 'author', 'post'}
    success_url = '/'
