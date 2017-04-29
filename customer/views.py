from django.shortcuts import render


from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from .forms import UserForm, LoginForm
from django.contrib import messages


def user_login(request):
    whereami = 'login'
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('vegetables:vegetable_view'))
    form = LoginForm(request.POST or None)
    context = {'form': form}

    if request.POST:

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:

            if user.is_active:
                login(request, user)
                messages.add_message(request, messages.INFO, 'Successfully Logged in !')
                return redirect('vegetables:vegetable_view')

    return render(request, 'customer/login.html', context)


class UserFormView(View):
    form_class = UserForm
    template_name = 'customer/registration_form.html'
    atregister = True

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'atregister': self.atregister})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('vegetables:vegetable_view')
        return render(request, self.template_name, {'form': form})


def user_logo(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(request, messages.INFO, "Successfully Logged Out")
        return HttpResponseRedirect(reverse('vegetables:vegetable_view'))
    else:
        messages.add_message(request, messages.INFO, "You were not logged in.")
        return HttpResponseRedirect(reverse('vegetables:vegetable_view'))
