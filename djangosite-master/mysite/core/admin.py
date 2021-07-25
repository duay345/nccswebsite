from django.contrib import admin

from .models import info
from .models import Intro
from .models import mydoc
from .models import profile
from .models import skills
from .models import Comment 
from .models import Aboutyou
# Register your models here.

admin.site.register(info)
admin.site.register(Intro)
admin.site.register(mydoc)
admin.site.register(profile)
admin.site.register(skills)
admin.site.register(Comment)
admin.site.register(Aboutyou)


#@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)