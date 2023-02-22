from django.contrib import admin
from product.models import Product, Hashtag, Comment

admin.site.register(Product)
admin.site.register(Hashtag)
admin.site.register(Comment)
