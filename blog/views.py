from django.shortcuts import render, get_object_or_404, redirect  
from django.utils import timezone  
from django.contrib.auth.decorators import login_required  
from django.contrib import messages  
from .models import Post  
from .forms import PostForm  
from likes.models import Like  

# View to display a list of blog posts
def post_list(request):
    """
    Retrieves all blog posts with a published date up to the current time, 
    orders them by published date in descending order, and renders the post list template.
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})  

# View to display the details of a specific post
def post_detail(request, pk):
    """
    Fetches a single post based on its primary key (pk) and checks if the user has liked it.
    Renders the post detail template with the post data and like status.
    """
    post = get_object_or_404(Post, pk=pk)  
    liked = False  

    # Check if the user is logged in and has liked the post
    if request.user.is_authenticated:  
        liked = Like.objects.filter(post=post, user=request.user).exists()  

    return render(request, 'blog/post_detail.html', {'post': post, 'liked': liked})  #

# View to create a new post, restricted to logged-in users
@login_required
def post_new(request):
    """
    Handles the creation of a new post. If the request method is POST, 
    validates and saves the form data as a new post, setting the author 
    and published date. If GET, displays a blank form.
    """
    if request.method == "POST":  
        form = PostForm(request.POST, request.FILES)  
        if form.is_valid():  
            post = form.save(commit=False)  
            post.author = request.user  
            post.published_date = timezone.now()  
            post.save()  
            messages.success(request, "Your post has been successfully created.")  
            return redirect('post_detail', pk=post.pk)  
    else:
        form = PostForm()  
    return render(request, 'blog/post_edit.html', {'form': form})  

# View to edit an existing post, restricted to logged-in users
@login_required
def post_edit(request, pk):
    """
    Handles editing an existing post. If the request method is POST, 
    validates and saves the form data, updating the post. If GET, displays the form with the post's current data.
    """
    post = get_object_or_404(Post, pk=pk)  
    
    # Check if the user is either the post author or a superuser
    if request.user != post.author and not request.user.is_superuser:
        messages.error(request, "You do not have permission to edit this post.")
        return redirect('post_detail', pk=pk)

    if request.method == "POST":  
        form = PostForm(request.POST, request.FILES, instance=post)  
        if form.is_valid():  # Validate the form
            post = form.save(commit=False)  
            post.author = request.user  
            post.published_date = timezone.now()  
            post.save()  
            messages.success(request, "Your post has been successfully updated.")  
            return redirect('post_detail', pk=post.pk)  
    else:
        form = PostForm(instance=post)  
    return render(request, 'blog/post_edit.html', {'form': form})  
