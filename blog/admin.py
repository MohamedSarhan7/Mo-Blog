from django.contrib import admin
from .models import Post,Author,Tag,Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=("title","author","date",)
    list_filter=("tags","author","date",)
    prepopulated_fields={"slug":("title",)}
    
    
class AuthorAdmin(admin.ModelAdmin):
    list_display=("full_name","email")    
    readonly_fields=("full_name",)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "user_name", "date")
    list_filter=("post",)
 


admin.site.register(Post,PostAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
