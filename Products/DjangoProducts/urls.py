from django.urls import path
from .views import ProductListView

from . import views


urlpatterns = [
    path("", ProductListView.as_view(), name="get_products"),
    path("add_product/", views.add_product, name="add_product"),
    path("delete_product/<int:id>/", views.delete_product, name="delete_product"),
]