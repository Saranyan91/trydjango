from django.urls import include, path
from .views import (
    product_detail_view,
    product_create_view,
    product_delete_view,
    product_list_view,
    dynamic_lookup_view,
    product_update_view
)
app_name = 'products'
urlpatterns = [
    path('create/', product_create_view),
    path('<int:id>/update/', product_update_view, name='product-update'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
    path('', product_list_view, name='product-list'),
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
]
