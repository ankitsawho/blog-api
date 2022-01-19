from django.contrib import admin
from .models import Post, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    list_display = ['id', 'title', 'createdAt']
    summernote_fields = ('content',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
