from django.urls import path
from social.views import PostListView

urlpatterns = [
    path("", PostListView.as_view(), name='post-list'),
]