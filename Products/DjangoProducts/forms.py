from django import forms
from .models import Product



class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}), label="Назва товару")
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}), label="Опис товару")
    price = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}), label="Ціна товару")

    class Meta:
        model = Product
        fields = ("name", "description", "price")


