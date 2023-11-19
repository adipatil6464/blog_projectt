from django.db import models
from tinymce.models import HTMLField

class Category(models.Model):
    cat_Id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,default='category')
    description = HTMLField()
    url = models.CharField(max_length=100)
    img = models.ImageField(upload_to='category')
    add_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    post_Id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = HTMLField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='post')

    def __str__(self) -> str:
        return self.title

class UserAdmin(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    

    
# Create your models here.
