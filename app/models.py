from django.db import models
from django.utils.html import format_html
import uuid
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.core.files.base import ContentFile
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
        ('light','Light'),
        ('warning','Yellow'),
         ('info','Sky Blue'),
         ('secondary ','Grey'),
       ]
    cat_id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    color=models.CharField(max_length=32,choices=CHOICES,default='Black' ,verbose_name="Chuse categry color")
    description=models.TextField()
    url=models.CharField(max_length=100)
    image=models.ImageField(upload_to='category/')
    add_date =models.DateField(auto_now_add=True,null=True)
 
    def save(self, *args, **kwargs):
        if self.image:
           
            self.resize(self.image, (300, 200))
         
         
        super(Category, self).save(*args, **kwargs)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;" /> ' .format(self.image))
    def __str__(self):
        return self.title

class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content = models.TextField()
    url=models.CharField(max_length=100)
    cat=models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='Post/')   
    add_date =models.DateField(auto_now_add=True,null=True)
 
    def __str__(self):
        return self.title

# class PostContent(models.Model):
    # content_id=models.AutoField(primary_key=True)
    # title=models.CharField(max_length=200)
    # content = models.TextField()

    # url=models.CharField(max_length=100)
    # post=models.ForeignKey(Post, on_delete=models.CASCADE)
    # image=models.ImageField(upload_to='Post/')

#post mode


class activity(models.Model):
    activity_id=models.AutoField(primary_key=True)
    likes=models.IntegerField()
    comments = models.TextField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    class Meta:
        ordering = ['created_on']

        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def __str__(self):
        return 'Comment {} by {}'.format(self.comments, self.name)
        
   

  
