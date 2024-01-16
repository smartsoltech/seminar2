from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Product, Order
from .forms import ClientForm, ProductForm, OrderForm
from .logger import log_function_call, logging

logger = logging.getLogger(__name__)
def start_view(request):
    return render(request, 'base.html')

# Client Views


@log_function_call(logger)
def client_view(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'client_view.html', {'client': client})

@log_function_call(logger)
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

@log_function_call(logger)
def client_create(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('client_list')
    return render(request, 'client_form.html', {'form': form})

@log_function_call(logger)
def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('client_list')
    return render(request, 'client_form.html', {'form': form})


@log_function_call(logger)
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'client_delete.html', {'client': client})

# Product Views

@log_function_call(logger)
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@log_function_call(logger)
def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', {'product': product})

@log_function_call(logger)
def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product_form.html', {'form': form})

@log_function_call(logger)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_delete.html', {'product': product})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product_form.html', {'form': form})

# Order Views
# Аналогичные функции для Order

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def order_create(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('order_list')
    return render(request, 'order_form.html', {'form': form})

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    form = OrderForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('order_list')
    return render(request, 'order_form.html', {'form': form})

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'order_delete.html', {'order': order})

def order_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'order_view.html', {'order': order})
