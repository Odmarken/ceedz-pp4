from django.shortcuts import redirect
from .models import Like
from blog.models import Post

def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()  
    return redirect(post.get_absolute_url())
