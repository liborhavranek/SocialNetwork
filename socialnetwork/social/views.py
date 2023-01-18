from django.shortcuts import render
from django.views import View
from .models import Post
from .forms import PostForm, CommentForm
from django.http import JsonResponse
from django.utils import timezone
# Create your views here.


# class PostListView(View):
#     def get(self, request, *args, **kwargs):
#         posts = Post.objects.all().order_by('-created_on')
#         form = PostForm()
        
#         context = {
#             'post_list': posts,
#             'form': form,
#         }
        
#         return render(request, 'social/post_list.html', context)
    
#     def post(self, request, *args, **kwargs):
#         posts = Post.objects.all().order_by('-created_on')
#         form = PostForm(request.POST)
        
#         if form.is_valid():
#             new_post = form.save(commit=False)
#             new_post.author = request.user
#             new_post.save()
            
#         context = {
#             'post_list': posts,
#             'form': form,
#         }
        
#         return render(request, 'social/post_list.html', context)
    
    
    
    
class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()
        
        context = {
            'post_list': posts,
            'form': form,
        }
        
        return render(request, 'social/post_list.html', context)
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.created_on = timezone.now()
            new_post.save()
            return JsonResponse({"new_post":new_post.body,
                                 "post_author": new_post.author.username,
                                 "post_time_created":new_post.created_on
                                 })

    
    
class PostDetailView(View): 
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        
        context = {
            'post': post,
            'form': form,
            }
        return render(request, 'social/post_detail.html', context)