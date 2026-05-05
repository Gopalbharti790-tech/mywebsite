from django.urls import path
from . import views

urlpatterns=[
    path("", views.homepage, name='home'),
    path("allposts/",views.blogposts, name='allpost'),
    path("allposts/about", views.about , name='about'),
    path("allposts/contact", views.contact , name='contact'),
    
    path("allposts/<slug:blog>",views.blog_posts,name='blog-post')
]