from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.contrib.auth.decorators import login_required



#Create your views here.
def post_list(request, cat):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__contains=cat).order_by('published_date')
    return render(request, 'Memetropolis/homepage.html',  {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Memetropolis/post_detail.html', {'post': post})
    from django.shortcuts import redirect
    return redirect('post_detail', pk=post.pk)
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'Memetropolis/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'Memetropolis/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'Memetropolis/post_draft_list.html', {'posts': posts})

def explore(request):
    return render(request, 'Memetropolis/explore.html')
