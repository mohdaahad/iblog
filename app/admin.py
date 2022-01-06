from django.contrib import admin
from .models import Category,Post,activity
# Register your models here.
class ActivityAdmin(admin.ModelAdmin):
    list_display=('likes','comments')
    actions = ['approve_comments']
    def approve_comments(self, request, queryset):
        queryset.update(active=True)   
     
class CategoryAdmin(admin.ModelAdmin):
    list_display=('image_tag','title','description','url','add_date','color')
    search_fields=('title',)
    class Meta:
        # db_table = 'state'
        # Add verbose name
        verbose_name = 'Categories'
    
class PostAdmin(admin.ModelAdmin):
    list_display=('title',)
    search_fields=('title',)
    list_filter =('cat',)
    list_per_page =50
    
    class Media:
        js=('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js','js/script.js',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(activity,ActivityAdmin)

