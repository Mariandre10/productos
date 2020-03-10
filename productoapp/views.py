from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, ProductForm
from .models import Producto
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.

def log_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'productoapp/login.html', {'form':LoginForm})
    return render(request, 'productoapp/login.html', {'form':LoginForm})

def log_out(request):
    logout(request)
    return redirect('log_in')

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'productoapp/login.html', {'form':LoginForm})
    else:
        return render(request, 'productoapp/home.html')

def table(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    productos = Producto.objects.order_by('name')
    print(productos)
    return render(request, 'productoapp/table.html', {'productos':productos,'form':ProductForm})

def charts(request):
    if not request.user.is_authenticated:
        return render(request, 'productoapp/login.html', {'form':LoginForm})
    else:
        return render(request, 'productoapp/charts.html')

def delete_product(request, pk):
    producto = Producto.objects.get(id=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('table')
    return render(request, 'productoapp/delete_product.html', {'form':ProductForm})

def edit_product(request, pk):
    producto = Producto.objects.get(id=pk)
    if request.method == 'GET':
        form = ProductForm(instance=producto)
    else:
        form = ProductForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('table')
    return render(request,'productoapp/edit_product.html',{'form':form})