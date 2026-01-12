from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.models import User

def timeline(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            
            # ユーザーを割り当てる（エラー回避のため）
            first_user = User.objects.first()
            if first_user:
                post.author = first_user
            
            post.save()
            return redirect('timeline') # ← ここもインデントが必要
    else:
        form = PostForm()
    
    posts = Post.objects.all().order_by('-created_at')
    # ↓ この return の行頭にスペース4つ（またはタブ1つ）が必要です
    return render(request, 'post_index.html', {'form': form, 'posts': posts})