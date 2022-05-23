from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from blog.models import Post, Comment, Category, Tag, Blog


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = 'title', 'content', 'category', 'tags', 'avatar'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class Category(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'


class LoginForm(AuthenticationForm):
    login = forms.CharField(label='Login', max_length=20, min_length=3)
    password = forms.CharField(label='Password', max_length=20, min_length=6, widget=forms.PasswordInput)


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('name',)


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', "password1", "password2")
