from django.contrib import admin

# Register your models here.
from home.models import Category, Home, Images

class HomeImageInline(admin.TabularInline):
    model = Images
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'image_tag', 'status']
    list_filter = ['status']
    inlines = [HomeImageInline]
    readonly_fields = ('image_tag',)

class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'home', 'image_tag']
    readonly_fields = ('image_tag',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.register(Images, ImageAdmin)
