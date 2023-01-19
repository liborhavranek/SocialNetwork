from django.urls import path
from social.views import PostListView, PostDetailView, PostEditVIew, PostDeleteView

urlpatterns = [
    path("", PostListView.as_view(), name='post-list'),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("post/edit/<int:pk>", PostEditVIew.as_view(), name="post-edit"),
    path("post/delete/<int:pk>", PostDeleteView.as_view(), name="post-delete"),
    
]