import os
import django
import random
from faker import Faker
from datetime import timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seminar2.settings")
django.setup()

from shop.models import Client, Product, Order, OrderItem  # Измените на ваш путь

fake = Faker()

# Генерация клиентов
for _ in range(100):
    Client.objects.create(
        name=fake.name(),
        email=fake.email(),
        phone_number=f'+{fake.random_number(digits=10, fix_len=True)}',
        address=fake.address()
    )

# Генерация товаров
for _ in range(100):
    Product.objects.create(
        name=fake.word(),
        description=fake.text(),
        price=random.uniform(10, 500),
        quantity=random.randint(1, 100),
        added_date=fake.date_time_this_year()
    )

# Генерация заказов
clients = Client.objects.all()
products = list(Product.objects.all())

for _ in range(500):
    order_date = fake.date_time_this_year()
    order = Order.objects.create(
        client=random.choice(clients),
        total_amount=0,  # Первоначально 0, будет обновлено
        order_date=order_date
    )
    
    # Добавление продуктов в заказ
    total_amount = 0
    for _ in range(random.randint(1, 5)):  # От 1 до 5 товаров в заказе
        product = random.choice(products)
        quantity = random.randint(1, 3)
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity
        )
        total_amount += product.price * quantity

    # Обновление общей суммы заказа
    order.total_amount = total_amount
    order.save()
