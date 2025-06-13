from django.shortcuts import render
from feedback.forms import FeedbackForm
from goods.models import Products


def index(request):
    feedback_form = FeedbackForm()

    # Лучшая цена (максимальная скидка, при равных - максимальная цена)
    best_price = (
        Products.objects.filter(discount__gt=0).order_by("-discount", "-price").first()
    )

    # Новинка недели (последние добавленные)
    new_week = Products.objects.order_by("-created_at", "-price").first()

    # Скоро закончится (минимальное количество)
    ending_soon = (
        Products.objects.filter(quantity__gt=0).order_by("quantity", "-price").first()
    )

    context: dict[str, str] = {
        "title": "S-GeForce - Главная",
        "content": "Интернет магазин",
        "content2": "компании S-GeForce",
        "slogan": "Лучшие комплектующие — для лучших сборок!",
        "feedback_form": feedback_form,
        "best_price": best_price,
        "new_week": new_week,
        "ending_soon": ending_soon,
    }
    return render(request, "main/index.html", context)
