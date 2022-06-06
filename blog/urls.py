from django.urls import URLPattern, path
from .views import BlogListView, BlogDetailView, CreatePost, UpdatePost, DeletePost

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/create/', CreatePost.as_view(), name='create_post'),
    path('post/<int:pk>/edit/', UpdatePost.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', DeletePost.as_view(), name='delete_post'),

]