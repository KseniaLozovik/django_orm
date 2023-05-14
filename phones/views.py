from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_value = request.GET.get('sort')
    template = 'catalog.html'
    if sort_value == 'min_price':
        phone = Phone.objects.order_by('price')
    elif sort_value == 'max_price':
        phone = Phone.objects.order_by('-price')
    elif sort_value == 'name':
        phone = Phone.objects.order_by('name')
    elif sort_value == None:
        phone = Phone.objects.order_by('id')
    context = {
        'phones': phone,
     }

    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    # print(phone)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)

