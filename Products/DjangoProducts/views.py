from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Product
from .forms import ProductForm

# Create your views here.


def add_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            messages.add_message(request=request, level=messages.SUCCESS, message="Товар успішно додано!")
            return redirect("get_products")

    return render(request=request, template_name="add_product.html", context=dict(form=form))


def get_products(request):
    products = Product.objects.all()
    return render(request=request, template_name="products.html", context=dict(products=products))


def delete_product(request, id):
    product = Product.objects.filter(pk=id).first()
    product.delete()
    messages.add_message(request=request, level=messages.SUCCESS, message=f"Товар '{product}' успішно видалено")
    return redirect("get_products")