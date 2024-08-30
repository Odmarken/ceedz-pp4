# likes/views.py

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from blog.models import Post
from .models import Like
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@csrf_exempt  # Use this if you're not handling CSRF in your JavaScript for simplicity
@login_required
def like_post(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        # Check if user has already liked the post
        liked = Like.objects.filter(post=post, user=user).exists()

        if not liked:
            # Create a new like
            Like.objects.create(post=post, user=user)
            liked = True
        else:
            # Remove the like
            Like.objects.filter(post=post, user=user).delete()
            liked = False

        # Return a JSON response with the updated like status and count
        likes_count = post.likes.count()
        return JsonResponse({'success': True, 'liked': liked, 'likes_count': likes_count})

    return JsonResponse({'success': False})
