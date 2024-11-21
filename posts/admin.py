from django.contrib import admin
from .models import Post


@admin.register(Post)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id", "content", "img", "created_at"]
