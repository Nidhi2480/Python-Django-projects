from django.shortcuts import render
from django.shortcuts import render
from MovieAPP.models import Movies
from django.db.models import Q

# Create your views here.
def searchPROD(request):
    query=None
    result=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        result=Movies.objects.all().filter(Q(Movie_Title__icontains=query) | Q(Description__icontains=query))
    return render(request,'search.html',{'query': query,'Movies':result})

# Create your views here.
