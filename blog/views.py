from django.shortcuts import render, get_object_or_404, redirect  
from django.utils import timezone  
from django.contrib.auth.decorators import login_required  
from .models import Post  
from .forms import PostForm  
from likes.models import Like  

# View to display a list of blog posts
def post_list(request):
    """
    Retrieves all blog posts with a published date up to the current time, 
    orders them by published date in descending order, and renders the post list template.
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')  #
    return render(request, 'blog/post_list.html', {'posts': posts})  

# View to display the details of a specific post
def post_detail(request, pk):
    """
    Fetches a single post based on its primary key (pk) and checks if the user has liked it.
    Renders the post detail template with the post data and like status.
    """
    post = get_object_or_404(Post, pk=pk)  # Fetch the post by primary key or return a 404 if not found
    liked = False  # Initialize liked status to False

    # Check if the user is logged in and has liked the post
    if request.user.is_authenticated:  # Check if the user is authenticated
        liked = Like.objects.filter(post=post, user=request.user).exists()  # Check if a like from this user exists for the post

    return render(request, 'blog/post_detail.html', {'post': post, 'liked': liked})  # Render the post detail template with post and like data

# View to create a new post, restricted to logged-in users
@login_required
def post_new(request):
    """
    Handles the creation of a new post. If the request method is POST, 
    validates and saves the form data as a new post, setting the author 
    and published date. If GET, displays a blank form.
    """
    if request.method == "POST":  # Check if the form has been submitted
        form = PostForm(request.POST, request.FILES)  # Initialize the form with POST data and files for image uploads
        if form.is_valid():  # Validate the form
            post = form.save(commit=False)  # Create a new Post instance without saving to the database yet
            post.author = request.user  # Set the current user as the author of the post
            post.published_date = timezone.now()  # Set the published date to the current time
            post.save()  # Save the post to the database
            return redirect('post_detail', pk=post.pk)  # Redirect to the detail view of the newly created post
    else:
        form = PostForm()  # If the request method is GET, initialize an empty form
    return render(request, 'blog/post_edit.html', {'form': form})  # Render the post edit template with the form

# View to edit an existing post, restricted to logged-in users
@login_required
def post_edit(request, pk):
    """
    Handles editing an existing post. If the request method is POST, 
    validates and saves the form data, updating the post. If GET, displays the form with the post's current data.
    """
    post = get_object_or_404(Post, pk=pk)  # Fetch the post by primary key or return a 404 if not found
    if request.method == "POST":  # Check if the form has been submitted
        form = PostForm(request.POST, request.FILES, instance=post)  # Initialize the form with POST data, files, and the existing post instance
        if form.is_valid():  # Validate the form
            post = form.save(commit=False)  # Update the Post instance without saving to the database yet
            post.author = request.user  # Set the current user as the author of the post
            post.published_date = timezone.now()  # Update the published date to the current time
            post.save()  # Save the updated post to the database
            return redirect('post_detail', pk=post.pk)  # Redirect to the detail view of the updated post
    else:
        form = PostForm(instance=post)  # If the request method is GET, initialize the form with the existing post data
    return render(request, 'blog/post_edit.html', {'form': form})  # Render the post edit template with the form
