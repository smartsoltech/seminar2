from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Product, Order
from .forms import ClientForm, ProductForm, OrderForm, OrderFilterForm
from .logger import log_function_call, logging
from django.utils import timezone
from datetime import timedelta

logger = logging.getLogger(__name__)

def start_view(request):
    return render(request, 'base.html')


def order_view(request):
    form = OrderFilterForm(request.GET)
    orders = Order.objects.all()

    if form.is_valid():
        choice = form.cleaned_data.get('time_period')

        if choice == 'week':
            date_from = timezone.now() - timedelta(days=7)
        elif choice == 'month':
            date_from = timezone.now() - timedelta(days=30)
        elif choice == 'year':
            date_from = timezone.now() - timedelta(days=365)
        elif choice == 'all':
            date_from = None

        if date_from:
            orders = orders.filter(created_at__gte=date_from)

    return render(request, 'order_view.html', {'form': form, 'orders': orders})


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

@log_function_call(logger)
def product_update(request, pk):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Действия после сохранения формы, например, перенаправление
    else:
        form = ProductForm()

    return render(request, 'product_create.html', {'form': form})

# Order Views

@log_function_call(logger)
def order_list(request):
    form = OrderFilterForm(request.GET or None)
    orders = Order.objects.all()
    start_date = timezone.now() - timedelta(weeks=1)  # Для фильтра по умолчанию на одну неделю
    if form.is_valid():
        filter_choice = form.cleaned_data.get('time_filter')

        if filter_choice == 'week':
            start_date = timezone.now() - timedelta(weeks=1)
        elif filter_choice == 'month':
            start_date = timezone.now() - timedelta(weeks=4)
        elif filter_choice == 'year':
            start_date = timezone.now() - timedelta(weeks=52)

        orders = orders.filter(order_date__gte=start_date)

    return render(request, 'order_list.html', {'form': form, 'orders': orders})

@log_function_call(logger)
def order_create(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('order_list')
    return render(request, 'order_form.html', {'form': form})

@log_function_call(logger)
def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    form = OrderForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('order_list')
    return render(request, 'order_form.html', {'form': form})

@log_function_call(logger)
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'order_delete.html', {'order': order})

@log_function_call(logger)
def order_detail_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'order_detail.html', {'order': order})