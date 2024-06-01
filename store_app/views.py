from django.shortcuts import render
from .models import Category, Product
from django.http import JsonResponse
from .models import OrderItem
from django.shortcuts import redirect

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'store/home.html', context)

def supermarket(request):
    return render(request, 'store/supermarket.html')

def get_products_by_category(request, category_id):
    print(category_id)
    categories = Category.objects.all()
    selected_category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=selected_category)
    products_data = []
    for product in products:
        product_data = {
            "id": product.id,
            # "category": product.category,
            "name": product.name,
            "imageURL": product.imageURL,  # Assuming you have an imageURL field
            "price": product.price,
            # ... Add other product data you want to display
        }
        products_data.append(product_data)
    
    return JsonResponse(products_data, safe=False)  # Set safe=False if including non-string data

def update_cart(request):
    item_id = request.GET.get('item_id')
    new_quantity = int(request.GET.get('quantity'))

    # Update the quantity of the item in the database
    item = OrderItem.objects.get(id=item_id)
    item.quantity = new_quantity
    item.save()

    # Return a JSON response indicating success
    return JsonResponse({'message': 'Cart updated successfully'})