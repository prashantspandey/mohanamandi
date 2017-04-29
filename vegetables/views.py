from django.shortcuts import render
from .models import Vegetable


def vegetable_view(request):
    # boolean for active tabs (front end)
    user = request.user

    atvegetable = True
    all = Vegetable.objects.all()
    context = {'vegetables': all, 'atvegetable': atvegetable}
    return render(request, 'vegetables/vegView.html', context)
