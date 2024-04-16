from django.shortcuts import render
from .models import Category, Product
from django.http import JsonResponse

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'home.html', context)

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