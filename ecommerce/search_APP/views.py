from django.shortcuts import render
from ecommerceAPP.models import Product
from django.db.models import Q

# Create your views here.
def searchPROD(request):
    query=None
    result=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        result=Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    return render(request,'search.html',{'query': query,'products':result})
