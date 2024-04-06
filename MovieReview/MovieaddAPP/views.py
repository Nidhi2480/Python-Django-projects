from django.shortcuts import render, redirect
from .forms import MoviesForm
from MovieAPP.models import Movies
def add_movie(request):
        if request.method == 'POST':
            form = MoviesForm(request.POST, request.FILES)
            if form.is_valid():
                movie = form.save(commit=False)
                movie.user = request.user 
                movie.save()  
                return redirect('movie:allmovie')
        else:
            form = MoviesForm()
        return render(request, 'forms.html', {'form': form})


def update(request,id=None):
    if id!=None:
        obj=Movies.objects.get(id=id)
        forms=MoviesForm(request.POST or None,request.FILES,instance=obj )
        if forms.is_valid():
            forms.save()
            return redirect('movie:allmovie')
        return render(request,'edit.html',{'form':forms,'laptop':obj})
    else:
        use=request.user 
        obj=Movies.objects.filter(user=use)
        return render(request,'update.html',{'mov':obj})