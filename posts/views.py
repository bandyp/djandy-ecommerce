
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseForbidden, HttpResponse
from .models import Post
from .forms import BlogPostForm
from django.contrib.auth.models import User
from accounts.models import Profile
from accounts.forms import UserLoginForm, UserRegistrationForm, ProfileUpdateForm, UserUpdateForm

def get_posts(request):
    """
    Create a view of previous posts and render to a template
    """

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
    return render(request, "blogposts.html", {'posts': posts})


def post_detail(request, pk):
    """
    create a view that returns a single post using post ID and render to template or return a 404 error"
    """

    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})

def new_post(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == "POST":
            form = BlogPostForm(request.POST, request.FILES)
            if form.is_valid():
                
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('get_posts')
        else:
            form = BlogPostForm()


    return render(request, 'blogpostform.html', {'form': form})


def create_or_edit_post(request, pk=None):
    """
    create a view that allows to create or edit a post 
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    if (request.user.is_authenticated and request.user == post.author or request.user.is_superuser):
        if request.method == "POST":
            form = BlogPostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save()
                return redirect(post_detail, post.pk)
        else:
            form = BlogPostForm(instance=post)
    else:
        return HttpResponseForbidden()
        
    return render(request, 'blogpostform.html', {'form': form})
        
