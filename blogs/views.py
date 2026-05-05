
from django.shortcuts import render,reverse
from django.http import  HttpResponseNotFound, HttpResponseRedirect
from .models import Post_admin, contact
from .form import commentforms
from .contact_form import contactforms
# Create your views here.



def homepage(request):
   latest_blogs= Post_admin.objects.all().order_by("-date")[:2]
   return render(request,"index.html", {"l_blogs":latest_blogs})
   
def about (request):
   return render(request,"about.html" )


def contact (request):
   if request.method=="POST":
      contact_data=request.POST
      form=contactforms(contact_data)
      
      if form.is_valid():
         form.save()
         return HttpResponseRedirect(reverse("contact"))
      
      else:
         return HttpResponseNotFound("contact did not added")
     
   return render(request,"contact.html" )

def blogposts(request):
   blog_names = Post_admin.objects.all()
   return render(request,"allposts.html",{"blogs":blog_names})



def blog_posts(request, blog):
   post_data=Post_admin.objects.get(slug=blog)
   tags_caption=post_data.tags.all()
   form_data= commentforms()
   all_comments = post_data.comments.all().order_by("-id")

   if request.method =="POST":
      commented_data=request.POST
      form =commentforms(commented_data)
      
      if form.is_valid():
         comment=form.save(commit=False)
         comment.post= post_data
         comment.save()
         return HttpResponseRedirect(reverse("blog-post" ,args=[blog]))
      return render(request,"posts.html",{"post":post_data ,"tags":tags_caption,"comment":form , "comments":all_comments})
   
   else:   
      try:
         post_data=Post_admin.objects.get(slug=blog)
         tags_caption=post_data.tags.all()
         form_data= commentforms()
         return render(request,"posts.html",{"post":post_data ,"tags":tags_caption,"comment":form_data , "comments":all_comments})
      except:
         return HttpResponseNotFound("blog does not exist")
      