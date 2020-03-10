from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, ProductForm
from .models import Producto
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, RedirectView, FormView, View
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.

class Login(FormView):
    form_class= LoginForm
    template_name= "productoapp/login.html"

    def get_success_url(self):
        return reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request, *args, **kwargs)
    
    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

"""def log_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'productoapp/login.html', {'form':LoginForm})
    return render(request, 'productoapp/login.html', {'form':LoginForm})"""

class Logout(View):
    
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('log_in')) 

"""def log_out(request):
    logout(request)
    return redirect('log_in')"""

class Home(LoginRequiredMixin,ListView):
    template_name = "productoapp/home.html"
    model= Producto
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super(Home,self).get_context_data(**kwargs)
        form = ProductForm()
        context['form'] = form
        return context
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST.get('name')
            code = request.POST.get('code')
            fabricante = request.POST.get('fabricante')
            origen = request.POST.get('origen')
            precio= request.POST.get('precio')
            prod = Producto(name=name, code=code, fabricante=fabricante, origen=origen, precio=precio)
            prod.save()
            return redirect('home')

"""def home(request):
    if not request.user.is_authenticated:
        return render(request, 'productoapp/login.html', {'form':LoginForm})
    else:
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                form = ProductForm()
        productos = Producto.objects.order_by('name')
        return render(request, 'productoapp/home.html', {'productos':productos,'form':ProductForm})
        #return render(request, 'productoapp/home.html')"""

class EditProduct(LoginRequiredMixin,UpdateView):
    template_name = "productoapp/edit_product.html"
    model= Producto
    form_class = ProductForm
    success_url = reverse_lazy('home')

class DeleteProduct(LoginRequiredMixin,DeleteView):
    template_name = "productoapp/delete_product.html"
    model= Producto
    success_url = reverse_lazy('home')

"""def delete_product(request, pk):
    producto = Producto.objects.get(id=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('home')
    return render(request, 'productoapp/delete_product.html', {'form':ProductForm})"""

"""def edit_product(request, pk):
    producto = Producto.objects.get(id=pk)
    if request.method == 'GET':
        form = ProductForm(instance=producto)
    else:
        form = ProductForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'productoapp/edit_product.html',{'form':form})"""