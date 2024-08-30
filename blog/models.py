from django.db import models  
from django.utils import timezone  
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField  

# Define the Post model representing a blog post in the database
class Post(models.Model):
    # The title of the post, limited to 200 characters
    title = models.CharField(max_length=200)
    
    # The content of the post, stored as a text field with no length limit
    content = models.TextField()
    
    # ForeignKey linking each post to a specific user (author)
    # on_delete=models.CASCADE ensures that if the user is deleted, all related posts are also deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Date and time when the post was created; defaults to the current time
    created_date = models.DateTimeField(default=timezone.now)
    
    # Date and time when the post was published; can be left blank or null
    published_date = models.DateTimeField(blank=True, null=True)
    
    # Image field integrated with Cloudinary for storing images
    # 'image' is the descriptive name for the field, blank=True allows the field to be optional, and null=True allows the database to store a NULL if no image is uploaded
    image = CloudinaryField('image', blank=True, null=True)

    # Method to publish the post by setting the published date to the current time
    def publish(self):
        self.published_date = timezone.now()  # Sets the published_date to the current time
        self.save()  # Saves the changes to the database

    # String representation of the Post model, useful for the Django admin and shell
    def __str__(self):
        return self.title  # Returns the title of the post as its string representation
