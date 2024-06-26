from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('get-products-by-category/<int:category_id>/', views.get_products_by_category, name='get_products_by_category'),
    path('remove-from-cart/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('', supermarket, name='supermarket'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)