from django.contrib import admin

# Register your models here.
from .models import ContentModel,TagModel,EmailModel


class ContentInline(admin.TabularInline):
    model = ContentModel
    fields  =['title','article',]
class TagAdmin(admin.ModelAdmin):
    inlines = [
        ContentInline,
    ]
    list_display = ("catagory",)
    

class ContentAdmind(admin.ModelAdmin):
    list_display = ("title", "slug",)
    list_filter=('tag',)
    prepopulated_fields = {"slug": ("title",)} 



admin.site.register(ContentModel, ContentAdmind)
admin.site.register(TagModel,TagAdmin )
admin.site.register(EmailModel, )