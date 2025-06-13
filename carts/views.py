import json
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from carts.models import Cart
from goods.models import Products


def cart_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse({"success": True})

    return redirect(request.META["HTTP_REFERER"])


def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse({"success": True})

    return redirect(request.META["HTTP_REFERER"])


@login_required
def cart_update(request, cart_id):
    if request.method == "POST":
        cart = Cart.objects.get(id=cart_id, user=request.user)
        try:
            data = json.loads(request.body)
            change = int(data.get("quantity", 0))

            new_quantity = cart.quantity + change
            if new_quantity < 1:
                new_quantity = 1

            cart.quantity = new_quantity
            cart.save()

            return JsonResponse(
                {
                    "success": True,
                    "new_quantity": cart.quantity,
                    "product_total": cart.products_price(),
                    "total_quantity": cart.user.cart_set.total_quantity(),
                    "grand_total": cart.user.cart_set.total_price(),
                }
            )
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    return JsonResponse({"success": False, "error": "Invalid request"})


@login_required
def can_increase(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id, user=request.user)
    return JsonResponse({"can_increase": cart.can_increase()})
