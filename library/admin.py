from django.contrib import admin
from .models import Book, Loan, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Какие поля показывать в списке (колонки таблицы)
    list_display = ('title', 'author', 'isbn', 'inventory_count')
    # По каким полям можно искать
    search_fields = ('title', 'author', 'isbn')
    # Справа появится фильтр
    list_filter = ('author',)

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    # Показываем кто взял, что взял, когда, и статус (активна или нет)
    list_display = ('user', 'book', 'taken_at', 'returned_at', 'is_active')
    # Фильтры справа: показать только активные (должников) или по дате
    list_filter = ('is_active', 'taken_at')
    # Поиск по имени юзера или названию книги
    search_fields = ('user__username', 'book__title')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')