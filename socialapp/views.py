from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect

from .forms import PostForm
from .models import Profile, Post

@login_required
def home(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            profile, _ = Profile.objects.get_or_create(user=request.user)
            post.profile = profile
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'socialapp/home.html', {'posts': posts, 'form': form})


def profile_detail(request, username):
    user = get_object_or_404(User, username=username)
    profile, _ = Profile.objects.get_or_create(user=user)
    return render(request, 'socialapp/profile_detail.html', {'profile': profile})
