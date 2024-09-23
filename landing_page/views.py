from django.shortcuts import render

from product.models import Product
# Initial landing page view.
def index(request):

    products = Product.objects.all()

    return render(request, 'landing_page/index.html', {"products": products})


#Add other views here