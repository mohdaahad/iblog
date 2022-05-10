from django.contrib import admin
from .models import Category,Post,activity,Comment,User_Additional_detail
from django import template

register = template.Library()

@register.filter
def in_category(things, num):
    return things.filter(likes=num)

# Register your models here.y
# @admin.register(activity)
# @admin.register(Comment)
class User_Additional_detailAdmin(admin.ModelAdmin):
    list_display=('user_profile', 'user_id',  )

class ActivityAdmin(admin.ModelAdmin):
    list_display=( 'post', 'created_date')
    list_filter = ( 'created_date',)
    search_fields = ('name', )
    # actions = ['approve_comments']
    

class CommentAdmin(admin.ModelAdmin):
    list_display=('name',  'post', "text",'created_date')
    list_filter = ( 'created_date',)
    search_fields = ('name',"text")
    # actions = ['approve_comments']
   
    
class CategoryAdmin(admin.ModelAdmin):
    list_display=('user_id','title','description','url','created_date','color',)
    search_fields=('title','user_id')
    class Meta:
        # db_table = 'state'
        # Add verbose name
        verbose_name = 'Categories'
    
class PostAdmin(admin.ModelAdmin):
    list_display=('title','user_id')
    search_fields=('title','user_id')
    list_filter =('category',)
    list_per_page =50
    def save_model(self, request, obj, form, change) -> None:
        obj.created_by=request.user
        return super().save_model(request, obj, form, change)
    class Media:
        js=('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js','js/script.js',)

# admin.site.register(User_Additional_detail,User_Additional_detailAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(activity,ActivityAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(User_Additional_detail,User_Additional_detailAdmin)

