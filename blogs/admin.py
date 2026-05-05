from django.contrib import admin
from .models import Post_admin,Author,Tag, comments, contact


class postadmin(admin.ModelAdmin):
    list_filter = ("author","tags", "date")
    list_display =("title" , "date" ,"author" )
    prepopulated_fields = {"slug":("title",)}

class commentadmin(admin.ModelAdmin):
    list_display =("user_name","post_slug", "post")
    def post_slug(self,obj):
        return obj.post.slug
    
class contactadmin(admin.ModelAdmin):
    list_display =("user_name","user_email")
    


# Register your models here.
admin.site.register(Post_admin, postadmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(comments, commentadmin)
admin.site.register(contact, contactadmin)