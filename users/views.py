from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UploadProduct
from .forms import Product


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", { "form": form })

def logout_user(request):
     if request.method == 'POST':
        logout(request)
        return redirect('/')

@login_required(login_url="/users/login/")
def product_list_view(request): 
    if request.method == 'POST':
        form = UploadProduct(request.POST)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return redirect('users:producto')
    else:
        form = UploadProduct()

#lista de productos
    product_list = Product.objects.all()[:20]

    return render(request, "users/producto.html", {
        "product_list": product_list,
        "form": form
    })