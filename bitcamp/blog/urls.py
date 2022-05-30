from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    # path('posts/', posts, name="posts"),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>', post, name='post'),

    path('post_add/', post_add, name='post_add'),
    path('post/new/', PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category'),

    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
