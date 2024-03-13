from django.contrib import admin

from posts.models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')
    list_display_links = ('title',)
