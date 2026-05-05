from django.db import models

# Create your models here.
class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    e_mail= models.EmailField()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    
    def __str__(self):
        return self.get_full_name()


class Tag(models.Model):
    caption= models.CharField( max_length=20)

    def __str__(self):
        return self.caption
    


class Post_admin(models.Model):
    title= models.CharField(max_length=100)
    date= models.DateField(auto_now=True)
    preview= models.CharField(max_length=250)
    slug=models.SlugField(unique=True)
    content=models.TextField()
    img=models.CharField(max_length=50)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL, null=True)
    tags= models.ManyToManyField(Tag)


class comments(models.Model):
    user_name= models.CharField(max_length=50)
    user_email= models.EmailField()
    user_comments= models.CharField( max_length=250)
    post =models.ForeignKey(Post_admin , on_delete=models.CASCADE, related_name="comments")

class contact(models.Model):
    user_name= models.CharField(max_length=50)
    user_email= models.EmailField()
    message= models.CharField( max_length=250)
   
    def __str__(self):
       return self.user_name
   