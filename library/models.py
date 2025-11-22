from django.db import models
from django.utils import timezone
from django.conf import settings


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books", verbose_name="Автор"
    )
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    inventory_count = models.PositiveIntegerField(
        default=1, verbose_name="Количество в наличии"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Loan(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="loans", verbose_name="Книга"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="loans",
        verbose_name="Читатель",
    )
    taken_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата выдачи")
    returned_at = models.DateTimeField(
        null=True, blank=True, verbose_name="Дата возврата"
    )
    is_active = models.BooleanField(default=True, verbose_name="Книга на руках")

    def return_book(self):
        """Метод для возврата книги"""
        if self.is_active:  # если книга еще на руках
            self.returned_at = timezone.now()
            self.is_active = False  # книга возвращена
            self.book.inventory_count += 1
            self.book.save()
            self.save()

    def save(self, *args, **kwargs):
        # Если создается новая запись (выдача книги)
        if not self.pk and self.is_active:
            if self.book.inventory_count > 0:
                self.book.inventory_count -= 1
                self.book.save()
            else:
                raise ValueError("Книг нет в наличии")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Выдача книги"
        verbose_name_plural = "Выдача книг"
