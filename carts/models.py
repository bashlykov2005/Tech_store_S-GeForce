from django.db import models
from goods.models import Products

from users.models import User


class CartQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'cart'
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    objects = CartQueryset().as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    @classmethod
    def total_quantity(cls, user):
        return sum(cart.quantity for cart in cls.objects.filter(user=user))

    @classmethod
    def total_price(cls, user):
        return sum(cart.products_price() for cart in cls.objects.filter(user=user))

    def __str__(self):
        if self.user:
            return f'Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}'

        return f'Анонимная корзина | Товар {self.product.name} | Количество {self.quantity}'

        # метод для проверки, можно ли увеличить количество
    def can_increase(self):
        return self.quantity < self.product.quantity

    #  метод для форматированной цены
    def formatted_price(self):
        return f"{self.products_price():.2f} ₽"
