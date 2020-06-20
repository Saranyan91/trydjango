from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm

from .models import Product
# Create your views here.


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     # if form.is_valid():
#     #     form.save()
#     #     form = ProductForm()
#     context = {
#         'form': my_form
#     }
#     return render(request, "products/product_create.html", context)
def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)


def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)


def dynamic_lookup_view(request, id):
    obj = Product.objects.get(id=id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)
