from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.shortcuts import reverse
from .models import Cart
# from django.contrib.auth.decorators import login_required
from vegetables.models import Vegetable


def cart(request):
    user = request.user
    atcart = True
    if user.is_authenticated:
        # add specific item to cart
        if 'vegetableid' in request.POST:
            vegetableid = request.POST['vegetableid']
            quantity = request.POST['quantity']
            subornot = request.POST['subornot']

            veg = get_object_or_404(Vegetable, id=vegetableid)
            total = int(int(veg.pricekg) * int(quantity))
            totalsub = int(int(veg.subpricekg) * int(quantity))
            # creating either subscription or normal cart object
            if subornot == 'yes':
                newCart = Cart(carter=user, quantity=quantity, total=totalsub,
                               veg=veg)
            else:
                newCart = Cart(carter=user, quantity=quantity, total=total,
                               veg=veg)
            newCart.save()
            return HttpResponseRedirect(reverse('cart:cart'))
            # delete cart object
        elif 'delbutton' in request.POST:
            cartid = request.POST['delbutton']
            delitem = get_object_or_404(Cart, id=cartid)
            print(delitem)
            delitem.delete()
            return HttpResponseRedirect(reverse('cart:cart'))

        cartset = user.cart_set.all()

        grandTotal = 0  # stores grand total of cart (whether sub or normal)
        normalprice = 0  # stores total normal price of cart
        cartprice = []
        vegnprice = []  # stores vegetable normal prices

        for c in cartset:
            cartprice.append(c.total)
            vegnprice.append(c.veg.pricekg * int(c.quantity))

        for p in cartprice:
            grandTotal = grandTotal + p
        for np in vegnprice:
            normalprice = normalprice + np
        # how much money saved by being on subscription
        mSaved = normalprice - grandTotal
        context = {'cart': cartset, 'grandTotal': grandTotal, 'atcart': atcart,
                   'saved': mSaved}
        return render(request, 'cart/cart.html', context)
    else:
        return HttpResponseRedirect(reverse('customer:login'))
