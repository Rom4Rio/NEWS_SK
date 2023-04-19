from django.contrib import admin
from .models import Post, Category, PostCategory


class PostCategoryInLine(admin.TabularInline):
    model = PostCategory
    fk_name = 'postThrough'
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [PostCategoryInLine]
    # ist_filter = ('postCategory', 'dateCreation')
    # list_display = ('title', 'postCategory')
    list_filter = ('title', 'postCategory')
    search_fields = ('title', 'postCategory')


class CategoryAdmin(admin.ModelAdmin):
    inlines = [PostCategoryInLine]
    list_display = ('name',)


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price')

admin.site.register(Category)
admin.site.register(Post, PostAdmin)

# admin.site.unregister(CategoryAdmin)
