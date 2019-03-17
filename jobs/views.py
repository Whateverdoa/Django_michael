from django.shortcuts import render
from .models import Jobs


def michael(request):
    jobs = Jobs.objects
    return render(request, 'jobs/home_view.html', {'jobs': jobs})
