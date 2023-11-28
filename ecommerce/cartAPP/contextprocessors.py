from . models import Cart,CartItem
from .views import _cart_id_
def counter(request):
    count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.get(cart_id=_cart_id_(request))
            cartitems=CartItem.objects.filter(cart=cart)
            for cartitem in cartitems:
                count +=cartitem.quantity
        except cart.DoesNotExist:
            count=0
    return dict(count=count)


