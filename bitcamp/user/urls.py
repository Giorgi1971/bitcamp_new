from django.urls import path
from .views import *


app_name='user'
urlpatterns = [
    path('', AutorListView.as_view(), name='authors'),
    path('<int:pk>/mentor/', MentorPostsView.as_view(), name='profile'),
    path('<int:pk>/', AuthorDetailView.as_view(), name='author'),
    path('<int:pk>/update/', UpdateAuthorView.as_view(), name='author_update'),
    path('<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),

    path('login/', my_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),

]