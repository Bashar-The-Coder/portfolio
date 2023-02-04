from django.shortcuts import render
from .models import Profile, Education, Course, Experience,Project,Service,Testimonial 
# Create your views here.
def index(request):
    profile = Profile.objects.get(pk = 1)
    main_job_title = profile.main_job_title
    context = {"profile" : profile , "main_job_title" : main_job_title}

    return render(request, 'main/home.html', context)

def about(request):

    profile = Profile.objects.get(pk = 1)
    main_job_title = profile.main_job_title
    age = profile.age
    context = {"profile" : profile , "main_job_title" : main_job_title, "age" : age}
    return render(request, 'main/about.html', context)

def resume(request):
    return render(request, 'main/resume.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def services(request):
    return render(request, 'main/services.html')

def contact(request):
    return render(request, 'main/contact.html')