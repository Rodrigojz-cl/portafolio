# curriculumapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.curriculum_view, name='curriculum'),
    path('<int:curriculum_id>/', views.curriculum_detail, name='curriculum_detail'),
    
]
