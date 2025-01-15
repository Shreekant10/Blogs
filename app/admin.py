from django.contrib import admin

from .models import Category, Post, Tags


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
admin.site.register(Category, CategoryAdmin)


class TagTublerInline(admin.TabularInline):
    model = Tags
    
class PostAdmin(admin.ModelAdmin):
    inlines = [TagTublerInline]
    list_display = ['id', 'title', 'author', 'status', 'category', 'section', 'date', 'main_post']
    list_editable = ['status', 'category', 'section', 'main_post']
    search_fields = ['title','section', 'category__name']
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Tags)

