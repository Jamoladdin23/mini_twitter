from django.urls import path

from .views import PostListView, CommentListView, PostCreateView, CommentCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='post'),
    path('comment', CommentListView.as_view(), name='comment'),
    path('posts/add-post', PostCreateView.as_view(), name='add_post'),
    path('posts/add-comment', CommentCreateView.as_view(), name='add_comment'),
]
