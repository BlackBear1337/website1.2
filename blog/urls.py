from django.urls import path

from .views import PostList, PostCreate, EditView, PostDetails, PostDelete, MyPostView, PostComment, LoginUserView, \
    logout_view, register_view, BlogCreateView

app_name = 'demo'

urlpatterns = [
    path('', PostList.as_view(), name='index'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('<slug:name>/', MyPostView.as_view(), name='my_posts'),
    path('<slug:name>/post/create', PostCreate.as_view(), name='create'),
    path('edit/<int:pk>', EditView.as_view(), name='edit'),
    path('details/<int:pk>/', PostDetails.as_view(), name='details'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='delete'),
    path('comment/<int:pk>/', PostComment.as_view(), name='comment'),
    path('createblog/', BlogCreateView.as_view(), name='createblog')
]
