from django.shortcuts import render,redirect
from .models import Task
from django.urls import reverse_lazy
from .forms import Taskform
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.
class listview1(ListView):
    model=Task
    template_name='listview.html'
    context_object_name='obj'
class detailview1(DetailView,):
    model=Task
    template_name='detailview.html'
    context_object_name='obj'
class updateview1(UpdateView):
    model=Task
    #form_class=Taskform
    template_name='updateview.html'
    fields=('name','priority','date')
    #success_url=reverse_lazy('listview')
    def get_success_url(self):
        return reverse_lazy('detailview',kwargs={'pk':self.object.id})
class deleteview1(DeleteView):
    model=Task
    template_name='deleteview.html'
    success_url=reverse_lazy('listview')
def submit(request):
    if request.method=='POST':
        name=request.POST['task']
        priority=request.POST['priority']
        date=request.POST['date']
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return redirect('listview')
        
def index(request):
    obj=Task.objects.all()
    if request.method=='POST':
        name=request.POST['task']
        priority=request.POST['priority']
        date=request.POST['date']
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'index.html',{'task1':obj})

def delete(request,id):
    if request.method=='POST':
         obj=Task.objects.get(id=id)
         obj.delete()
         return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    obj=Task.objects.get(id=id)
    form=Taskform(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'task':obj})