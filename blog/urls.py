from django.urls import path

from .views import PostList, PostCreate, EditView, PostDetails, PostDelete, AdminPanelView, PostComment

app_name = 'demo'

urlpatterns = [
    path('', PostList.as_view(), name='index'),
    path('adminpanel/', AdminPanelView.as_view(), name='adminpanel'),
    path('create/', PostCreate.as_view(), name='create'),
    path('edit/<int:pk>', EditView.as_view(), name='edit'),
    path('details/<int:pk>/', PostDetails.as_view(), name='details'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='delete'),
    path('comment/', PostComment.as_view(), name='comment')
]
