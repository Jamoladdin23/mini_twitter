from django.views.generic import ListView, DetailView, CreateView

from posts.forms import PostsForm
from .models import Posts, Comment


class PostListView(ListView):
    model = Posts
    context_object_name = 'users'
    template_name = 'users/users_list.html'


class CommentListView(ListView):
    model = Comment
    extra_context = {'title': 'Posts of Users'}
    template_name = 'posts/comments_list.html'


class PostCreateView(CreateView):
    # model = Posts
    form_class = PostsForm
    template_name = 'posts/add_posts.html'
    # success_url = 'post'


class CommentCreateView(CreateView):
    form_class = PostsForm
    template_name = 'posts/add_comment.html'


# class PostDetailView(DetailView):
#     model = Posts
#     template_name = 'posts/posts_detail.html'
#     context_object_name = 'post'
