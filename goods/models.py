"""Module providing a function printing python version."""

from django.db import models
from django.utils import timezone
from users.models import User

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    full_specs = models.TextField(
        blank=True, null=True, verbose_name="Полные характеристики"
    )
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Изображение"
    )
    image1 = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Изображение 2"
    )
    image2 = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Изображение 3"
    )
    price = models.DecimalField(
        default=0, max_digits=9, decimal_places=2, verbose_name="Цена"
    )
    discount = models.DecimalField(
        default=0, max_digits=4, decimal_places=2, verbose_name="Скидка в %"
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Категория"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    favorites = models.ManyToManyField(User, related_name="favorites", blank=True)

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.name} Количество - {self.quantity}"

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price

    def get_main_image(self):
        return (
            self.image.url if self.image else "static/deps/images/Not found image.jpg"
        )

    def get_images(self):
        images = []
        if self.image:
            images.append(self.image.url)
        if self.image1:
            images.append(self.image1.url)
        else:
            images.append(self.get_main_image())
        if self.image2:
            images.append(self.image2.url)
        else:
            images.append(self.get_main_image())
        return images

        # метод для получения первого изображения
    def get_first_image(self):
        if self.image:
            return self.image.url
        return "static/deps/images/Not found image.jpg"

    def is_available(self):
        return self.quantity > 0

    @property
    def in_stock(self):
        """Возвращает строку о наличии товара"""
        if self.quantity == 0:
            return "Нет в наличии"
        elif self.quantity < 5:
            return f"Осталось {self.quantity} шт."
        return "В наличии"

    def can_increase(self):
        return self.quantity < self.product.quantity
