from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from blog.forms import CommentForm, PostForm
from blog.models import Post, Comment, Blog


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


class MyPostView(LoginRequiredMixin, ListView):
    context_object_name = 'post'
    template_name = 'blog/mypost.html'
    login_url = reverse_lazy('demo:login')
    extra_context = {'title': 'My Posts'}

    def get_queryset(self):
        return Post.objects.filter(blog__slug=self.kwargs['name'])


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    login_url = reverse_lazy('demo:login')
    template_name = 'blog/post_create.html'
    extra_context = {'title': 'Create post'}
    context_object_name = 'form'
    fields = {'title', 'content', 'draft', 'category', 'tags', 'avatar'}
    slug_field = 'post_create_slug'

    def test_func(self):
        blog_slug = self.kwargs['name']
        user = self.request.user
        blog = Blog.objects.get(slug=blog_slug)
        if blog.author.user != user:
            return False
        return True

    def post(self, request, *args, **kwargs):
        blog_name = kwargs['name']
        form = PostForm(data=request.POST)
        post = form.save(commit=False)
        post.blog = Blog.objects.get(slug=blog_name)
        post.save()
        return redirect('demo:index')


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


class PostComment(LoginRequiredMixin, CreateView):
    model = Comment
    login_url = reverse_lazy('demo:login')
    extra_context = {'title': 'Comment'}
    context_object_name = 'comment'
    template_name = 'blog/post_comment.html'
    fields = {'text'}
    success_url = '/'

    def post(self, request, pk, *args, **kwargs):
        form = CommentForm(request.POST)
        post = Post.objects.get(pk=pk)
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        form.save_m2m()
        return redirect('demo:details', pk=pk)


def logout_view(request):
    logout(request)
    return redirect('demo:index')


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('demo:login')
    template_name = 'blog/register.html'


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'blog/login.html'

    def get_success_url(self):
        return reverse_lazy('demo:index')
