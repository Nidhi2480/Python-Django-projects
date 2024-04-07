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


def update(request, id=None):
    if id is not None:
        obj = Movies.objects.get(id=id)
        if request.method == 'POST':
            form = MoviesForm(request.POST, request.FILES, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('movie:allmovie')
        else:
            form = MoviesForm(instance=obj)
        return render(request, 'edit.html', {'form': form, 'movie': obj})
    else:
        use = request.user
        obj = Movies.objects.filter(user=use)
        return render(request, 'update.html', {'mov': obj})

def delete(request, id):
    mov = Movies.objects.get(id=id)
    mov.delete()
    return redirect('movieadd:update')