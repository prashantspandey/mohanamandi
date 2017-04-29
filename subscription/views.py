from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Subscription, Subscription_VegetableList
from django.utils import timezone


def subscription_view(request):
    user = request.user
    try:
        user.subscription
        return HttpResponseRedirect(reverse('vegetables:vegetable_view'))
    except:
        context = {}
        return render(request, 'subscription/all_subscriptions.html', context)


def confirm_subscription(request):
    user = request.user

    if 'subtype' in request.POST:
        subtype = request.POST['subtype']
        if subtype == 'Silver':
            cost = 2200
            mLeft = 2000
        elif subtype == 'Gold':
            cost = 5500
            mLeft = 5000
        else:
            cost = 11500
            mLeft = 10000
        newSubscription = Subscription(subscriber=user, sub_type=subtype,
                                       cost=cost, moneyLeft=mLeft, dateStarted=timezone.now(), length=30)
        newSubscription.save()
        try:
            ucart = user.cart_set.all()
            ucart.delete()
        except:
            pass
        context = {'subtype': subtype}
    return render(request, 'subscription/confirm_subscription.html', context)
