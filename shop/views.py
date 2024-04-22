from django.shortcuts import render, redirect
from .models import Product, Category


# Create your views here.

def home_page(request, category_slug=None):
    products = Product.objects.all()
    categories = Category.objects.all()
    category = None
    if category_slug:
        category = Category.objects.get(slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'index.html',
                  {"products": products, "categories": categories, "category": category})


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, 'products/product_detail.html', {'product': product})


def add_cart(request, product_id):
    cart = request.session.get("cart", {})
    product = Product.objects.get(id=product_id)
    if 'products' not in cart:
        cart['products'] = []
    if 'first_product_id' not in cart:
        cart['first_product_id'] = product.id

    product_found = False
    for item in cart['products']:
        if item['id'] == product.id:
            item['quantity'] += 1
            product_found = True
            break
    if not product_found:
        cart['products'].append({
            "name": product.name,
            "description": product.description,
            'price': str(product.price),
            'image': product.image.url,
            'id': product.id,
            "quantity": 1
        })

    request.session['cart'] = cart
    return redirect('cart')


def cart_details(request):
    cart = request.session.get("cart", {})
    print(cart)
    total_price = 0
    for item in cart['products']:
        quantity = item['quantity']
        total_price += quantity * float(item['price'])
    return render(request, 'products/cart.html', {"cart": cart, 'total_price': total_price})


def decrease_quantity(request):
    cart = request.session.get('cart', {})
    product_id = int(request.POST.get('product_id'))

    if 'products' in cart:
        for item in cart['products']:
            if item['id'] == product_id and item['quantity'] > 0:
                item['quantity'] -= 1
                request.session.modified = True
                break  # Exit the loop after updating quantity for the specific product

    return redirect('cart')


def increase_quantity(request):
    cart = request.session.get("cart", {})
    product_id = int(request.POST.get('product_id'))

    if 'products' in cart:
        for item in cart['products']:
            if item['id'] == product_id:
                item['quantity'] += 1
                request.session.modified = True
                break  # Exit the loop after updating quantity for the specific product

    return redirect('cart')


def remove_product(request, product_id):
    cart = request.session.get('cart', {})

    if 'products' in cart:
        cart['products'] = [item for item in cart['products'] if item['id'] != product_id]
        request.session.modified = True

    return redirect('cart')
