from django.shortcuts import render, Http404, HttpResponseRedirect, reverse
from customer.forms import UserProfileForm
from customer.models import User_profile
from vegetableOrder.models import Vegetable_order


def confirm_order(request):
    user = request.user
    if user.is_authenticated:
        form = UserProfileForm(request.POST or None)
        cartobj = request.user.cart_set.all()

        grandTotal = 0
        total = []
        for c in cartobj:
            total.append(c.total)
        for i in total:
            grandTotal = grandTotal + i
        context = {'form': form, 'cart': cartobj, 'gt': grandTotal, }
        return render(request, 'vegetableOrder/confirm_order.html', context)
    else:
        raise Http404


def process_order(request):
    user = request.user
    if user.is_authenticated:
        try:
            prof = user.user_profile

            ordercart = request.user.cart_set.all()

            tot = []
            total = 0

            newVegetableOrder = Vegetable_order()
            newVegetableOrder.user = user

            vegname = ""
            quant = ""
            for i in ordercart:
                vegname += i.veg.name + ","
                quant += str(i.quantity) + ","
                tot.append(i.total)
            newVegetableOrder.name = vegname
            newVegetableOrder.quantity = quant

            for k in tot:
                total = total + k
            newVegetableOrder.total = total
            newVegetableOrder.moneySaved = 0

            newVegetableOrder.save()
            try:
                user.subscription.moneyLeft = user.subscription.moneyLeft - newVegetableOrder.total
                user.subscription.save()
            except:
                pass
            context = {'profile': prof, 'order': newVegetableOrder, 'user': user}
            ordercart.delete()

            return render(request, 'vegetableOrder/process_order.html',
                          context)
        except:
            form = UserProfileForm(request.POST or None)
            if form.is_valid():
                print('profile not found')
                fn = form.cleaned_data['first_name']
                sn = form.cleaned_data['last_name']
                add1 = form.cleaned_data['address_line1']
                add2 = form.cleaned_data['address_line2']
                pc = form.cleaned_data['pincode']
                city = form.cleaned_data['city']
                state = form.cleaned_data['state']
                profile = User_profile(user=request.user, first_name=fn,
                                       last_name=sn, address_line1=add1,
                                       address_line2=add2,
                                       pincode=pc, city=city, state=state)
                profile.save()
                profile = request.user.user_profile
                ordercart = request.user.cart_set.all()
                tot = []
                total = 0
                newVegetableOrder = Vegetable_order()

                newVegetableOrder.user = request.user
                vegname = ""
                quant = ""
                for i in ordercart:
                    vegname += i.veg.name
                    quant += str(i.quantity) + ","
                    tot.append(i.total)
                newVegetableOrder.name = vegname
                newVegetableOrder.quantity = quant
                for k in tot:
                    total = total + k
                newVegetableOrder.total = total
                newVegetableOrder.moneySaved = 0

                newVegetableOrder.save()
                try:
                    user.subscription.moneyLeft = user.subscription.moneyLeft - newVegetableOrder.total
                    user.subscription.save()
                except:
                    pass

                ordercart.delete()

                context = {'profile': profile, 'order': newVegetableOrder, 'user': user}
                return render(request, 'vegetableOrder/process_order.html', context)
            else:
                return HttpResponseRedirect(reverse('veg_order:confirm_order'))

    else:
        raise Http404

# def process_order(request):
#     if request.user.is_authenticated:
#         try:
#             profile = request.user.user_profile
#             print('profile found')
#             ordercart = request.user.cart_set.all()
#             tot = []
#             total = 0
#             newVegetableOrder = Vegetable_order()
#
#             newVegetableOrder.user = request.user
#             for i in ordercart:
#                 newVegetableOrder.name += i.veg.name
#                 newVegetableOrder.quantity += i.quantity
#                 tot.append(i.total)
#
#             for k in tot:
#                 total = total + k
#             newVegetableOrder.total = total
#             newVegetableOrder.moneySaved = 0
#
#             newVegetableOrder.save()
#
#             context = {'profile': profile, 'order': newVegetableOrder}
#             ordercart.delete()
#             return render(request, 'vegetableOrder/process_order.html', context)
#         except:
#             form = UserProfileForm(request.POST or None)
#             if form.is_valid():
#                 print('profile not found')
#                 fn = form.cleaned_data['first_name']
#                 sn = form.cleaned_data['last_name']
#                 add1 = form.cleaned_data['address_line1']
#                 add2 = form.cleaned_data['address_line2']
#                 pc = form.cleaned_data['pincode']
#                 city = form.cleaned_data['city']
#                 state = form.cleaned_data['state']
#                 profile = User_profile(user=request.user, first_name=fn,
#                                        last_name=sn, address_line1=add1,
#                                        address_line2=add2,
#                                        pincode=pc, city=city, state=state)
#                 profile.save()
#                 profile = request.user.user_profile
#                 ordercart = request.user.cart_set.all()
#                 tot = []
#                 total = 0
#                 newVegetableOrder = Vegetable_order()
#
#                 newVegetableOrder.user = request.user
#                 for i in ordercart:
#                     newVegetableOrder.name += i.veg.name
#                     newVegetableOrder.quantity += i.quantity
#                     tot.append(i.total)
#
#                 for k in tot:
#                     total = total + k
#                 newVegetableOrder.total = total
#                 newVegetableOrder.moneySaved = 0
#
#                 newVegetableOrder.save()
#
#                 context = {'profile': profile, 'order': newVegetableOrder}
#                 ordercart.delete()
#
#                 context = {'profile': profile, 'order': newVegetableOrder}
#                 return render(request, 'vegetableOrder/process_order.html', context)
#         return HttpResponseRedirect(reverse('veg_order:confirm_order'))
#
#     else:
#         raise Http404
