from django.contrib import admin
from blog.models import *

admin.site.register(Category)
admin.site.register(Post)

class AdminUser(admin.ModelAdmin):
    list_display=['user_name','password']


admin.site.register(UserAdmin,AdminUser)
# Register your models here.
