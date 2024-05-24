# curriculumapp/views.py
from django.shortcuts import render
from .models import Curriculum


def curriculum_view(request):
    curriculum = Curriculum.objects.all()
    return render(request, 'curriculumapp/curriculum.html', {'curriculum': curriculum})

def curriculum_detail(request): 
    curriculum = Curriculum.objects.all()
    return render(request, 'curriculumapp/curriculum_detail.html', {'curriculum': curriculum})

#curriculum_detail es para comentar experiencia 
