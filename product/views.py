from django.shortcuts import render
from product.models import Product

# Create your views here.


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        product = Product.objects.all()

        context = {
            'product': [
                {
                    'id': product.id,
                    'title': product.title,
                    'rate': product.rate,
                    'image': product.image,
                    'hashtags': product.hashtags.all
                }
                for product in product
            ]
        }

        return render(request, 'products/products.html', context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'comments': product.comments.all()
        }

        return render(request, 'products/detail.html', context=context)
