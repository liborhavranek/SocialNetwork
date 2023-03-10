from django.shortcuts import render
from django.views import View
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.http import JsonResponse
from django.utils import timezone
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.conf.global_settings import SESSION_COOKIE_AGE
import time
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
    
    
    
    
# class PostListView(View):
#     def get(self, request, *args, **kwargs):
#         posts = Post.objects.all().order_by('-created_on')
#         comments = Comment.objects.all().order_by('-created_on')
#         form = PostForm()
#         comment_form = CommentForm()
        
#         context = {
#             'post_list': posts,
#             'form': form,
#             'comments':comments,
#             'comment_form':comment_form,
#         }
        
#         return render(request, 'social/post_list.html', context)
    
#     def post(self, request, *args, **kwargs):
#         form = PostForm(request.POST)
#         pk = request.POST.get('pk')
#         if pk:
#             post = Post.objects.get(pk=pk)
#         else:
#             post = None
#             comment_form = CommentForm(request.POST)
#             comments = Comment.objects.filter(post=post).order_by('-created_on')
        
#         if form.is_valid() and not pk:
#             new_post = form.save(commit=False)
#             new_post.author = request.user
#             new_post.created_on = timezone.now()
#             new_post.save()
#             return JsonResponse({"new_post":new_post.body,
#                                  "post_author": new_post.author.username,
#                                  "post_time_created":new_post.created_on
#                                  })
            
        
        
#         elif comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.author = request.user
#             new_comment.post = post
#             new_comment.save()
            
            
#             return JsonResponse({"new_comment":new_comment.comment,
#                              "comment_author": new_comment.author.username,
#                              "comment_time_created":new_comment.created_on
#                              })
            


class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        comments = Comment.objects.all().order_by('-created_on')
        form = PostForm()
        comment_form = CommentForm()
        
        context = {
            'post_list': posts,
            'form': form,
            'comments':comments,
            'comment_form':comment_form,
        }
        
        return render(request, 'social/post_list.html', context)
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        pk = request.POST.get('pk')
        if pk:
            post = Post.objects.get(pk=pk)
        else:
            post = None
        comment_form = CommentForm(request.POST)
        comments = Comment.objects.filter(post=post).order_by('-created_on')
        
        if form.is_valid() and not pk:
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.created_on = timezone.now()
            new_post.save()
            return JsonResponse({"new_post":new_post.body,
                                 "post_author": new_post.author.username,
                                 "post_time_created":new_post.created_on
                                 })
            
        
        
        elif comment_form.is_valid() and post:
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            
            
            return JsonResponse({"new_comment":new_comment.comment,
                             "comment_author": new_comment.author.username,
                             "comment_time_created":new_comment.created_on
                             })











    
class PostDetailView(View): 
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments':comments,
            }
        return render(request, 'social/post_detail.html', context)
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)
        
        if form.is_valid():
            new_coment = form.save(commit=False)
            new_coment.author = request.user
            new_coment.post = post
            new_coment.save()
        comments = Comment.objects.filter(post=post).order_by('-created_on')
        
        context = {
            'post': post,
            'form': form,
            'comments':comments,
            }
        return render(request, 'social/post_detail.html', context)
    
    
        
    
    
    
class PostEditVIew(UpdateView):
    model = Post
    fields = ['body']
    template_name = 'social/post_edit.html'
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk':pk})
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'social/post_delete.html'
    success_url = reverse_lazy('post-list')
    
