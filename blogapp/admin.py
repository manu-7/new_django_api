from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import CustomUser,Blog


class CustomUserAdmin(UserAdmin):
    list_display = ("username","first_name","last_name","profile_picture","bio","facebook","instagram","youtube")

admin.site.register(CustomUser,CustomUserAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_draft","category","created_at")
    
admin.site.register(Blog,BlogAdmin)