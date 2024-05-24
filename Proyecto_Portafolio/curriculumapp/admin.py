from django.contrib import admin
from django.urls import path, include
from .models import UserProfile

class UserProfile(admin.ModelAdmin):
    list_display = ('user', 'bio', 'avatar')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("contact/", include("contactapp.urls")),
    path("home/", include("homeapp.urls")),
]
# Register your models here.
