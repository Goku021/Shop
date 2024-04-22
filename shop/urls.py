from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name='home_page'),
    path("products/<slug:category_slug>/", views.home_page, name='home_page_by_categories'),
    path("product/<int:product_id>/", views.product_details, name='product_detail'),
    path("product/<int:product_id>/cart", views.add_cart, name='add_cart'),
    path("cart/", views.cart_details, name='cart'),
    path("cart/decrese_quantity", views.decrease_quantity, name='decrease_quantity'),
    path("cart/increase_quantity", views.increase_quantity, name='increase_quantity'),
    # path("cart/delete_item/<int:product_id>/", views.remove_product, name='remove'),
    path('remove/<int:product_id>/', views.remove_product, name='remove_product'),
]
