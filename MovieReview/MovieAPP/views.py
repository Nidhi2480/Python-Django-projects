from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout as auth_logout
from .models import Category,Movies
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def AllMovie(request,c_slug=None):
    c_page=None
    movie_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        movie_list=Movies.objects.all().filter(category=c_page)
    else:
        movie_list= Movies.objects.all()
    paginator=Paginator(movie_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        movies=paginator.page(page)
    except (EmptyPage,InvalidPage):
        movies = paginator.page(paginator.num_pages)

    return render(request,'category.html',{'category':c_page,'movies':movies})

def proddetail(request,c_slug,product_slug):
    try:
        mov=Movies.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        print('failed to fetch')
    return render(request,'product.html',{'movies':mov})
def login(request):
    message1={}
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('movie:allmovie')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
    else:
        return render(request,'login.html')



def register(request):
    request.session.pop('django.contrib.messages', None)
    if request.method == 'POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('movie:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('movie:register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                messages.success(request,'registration success')
                return redirect('movie:login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('movie:register')
    else:
        return render(request,'register.html')

def logout(request):
    auth_logout(request)
    return redirect('/')
