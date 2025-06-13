from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import logging
from goods.models import Products
from goods.utils import q_search


def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    # Сначала показываем товары по дате затем  с quantity > 0,
    goods = goods.order_by("-created_at", "-quantity")

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 6)
    current_page = paginator.page(int(page))

    context = {
        "title": "S-GeForce - Каталог",
        "goods": current_page,
        "slug_url": category_slug
    }
    return render(request, "goods/catalog.html", context)


@require_POST
@login_required
def toggle_favorite(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    user = request.user

    if user in product.favorites.all():
        product.favorites.remove(user)
        status = "removed"
    else:
        product.favorites.add(user)
        status = "added"

    return JsonResponse(
        {"status": status, "is_favorite": user in product.favorites.all()}
    )


def product(request, product_slug=False):

    product = Products.objects.get(slug=product_slug)

    context = {"title": f"{product.name} | S-GeForce", "product": product}

    return render(request, "goods/product.html", context=context)
