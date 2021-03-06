from django.contrib import admin
from django.utils import timezone
from .models import Post, Categroy, Tag


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'modified_time', 'category', 'author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.modified_time = timezone.now()
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
admin.site.register(Categroy)
admin.site.register(Tag)
