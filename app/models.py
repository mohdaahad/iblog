
from re import T
from PIL import Image
from django.db import models
from django.utils.html import format_html
import uuid
from PIL import Image

from io import BytesIO
from django.core.files import File
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
# Create your models here.
class ResizeImageMixin:
    def resize(self, imageField: models.ImageField, size:tuple):
        im = Image.open(imageField)  # Catch original
        source_image = im.convert('RGB')
        source_image.thumbnail(size)  # Resize to size
        output = BytesIO()
        source_image.save(output, format='JPEG') # Save resize image to bytes
        output.seek(0)

        content_file = ContentFile(output.read())  # Read output and create ContentFile in memory
        file = File(content_file)

        random_name = f'{uuid.uuid4()}.jpeg'
        imageField.save(random_name, file, save=False)

class Category(models.Model,ResizeImageMixin):
    CHOICES=[
        ('success','Green '),
        ('danger','Red'),
        ('dark','Black'),
        ('warning','Yellow'),
         ('info','Sky Blue'),
         ('primary','Blue'),
       ]
    # cat_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE,related_name='category')
    title = models.CharField(max_length=100)
    color=models.CharField(max_length=32,choices=CHOICES,default='Black' ,verbose_name="Chuse categry color")
    description=models.TextField()
    url=models.CharField(max_length=100)
    # image=models.ImageField(upload_to='category/')
    created_date =models.DateField(auto_now_add=True,null=True)
    updated_date =models.DateField(auto_now=True)
    Created_by = models.TextField(max_length=200,blank=True)
    updated_by = models.TextField(max_length=200,blank=True)
   
    class Meta:
        ordering = ['title']
 
    
    # def image_tag(self):
    #     return format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;" /> ' .format(self.image))
    def __str__(self):
        return self.title
   

class Post(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE,related_name='post', )
    # post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    category=models.ManyToManyField(Category)
    image=models.ImageField(upload_to='app/Post/')
    created_date =models.DateField(auto_now_add=True,null=True)
    updated_date =models.DateField(auto_now=True)
    Created_by = models.CharField(max_length=200,blank=True)
    updated_by = models.CharField(max_length=200,blank=True)
    # likes=models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='blogpost_like',blank=True)

    def number_of_likes(self):
        return self.likes.count()
    
    class Meta:
        ordering = ['title']
 
    def __str__(self):
        return self.title 




class activity(models.Model):
    # activity_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE,related_name='activity')
    likes=models.IntegerField(default=0)
    post=models.ForeignKey(Post, on_delete=models.CASCADE,related_name='activity')
   
    created_date =models.DateField(auto_now_add=True,null=True)
    updated_date =models.DateField(auto_now=True)
    Created_by = models.CharField(max_length=200,blank=True)
    updated_by = models.CharField(max_length=200,blank=True)
    class Meta:
        ordering = ['created_date']

        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def __str__(self):
        return f'like on {self.post.title}'
   
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comment')
    # user_id=models.ForeignKey(User, on_delete=models.CASCADE,related_name='comment')
    name = models.CharField(max_length=80)
    # email = models.EmailField()
    text = models.TextField()
    # created_on = models.DateTimeField(auto_now_add=True)
    # active = models.BooleanField(default=False)
    created_date =models.DateField(auto_now_add=True,null=True)
    updated_date =models.DateField(auto_now=True)
    Created_by = models.CharField(max_length=200,blank=True)
    updated_by = models.CharField(max_length=200,blank=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.text, self.name)




class User_Additional_detail(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_profile=models.ImageField(upload_to='app/userprofile/')
     

# resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.user_profile.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.user_profile.path)
    def __str__(self):
        return self.user_profile.url
   