from rest_framework import viewsets, permissions, status, mixins, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book, Loan, Author
from .serializers import BookSerializer, LoanSerializer, AuthorSerializer
from .permissions import IsAdminOrReadOnly


class AuthorViewSet(viewsets.ModelViewSet):
    """Класс авторов книг"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    """
    CRUD для книг.
    Админы могут всё, пользователи — только читать.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'isbn', 'author__last_name']


class LoanViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    """
    Управление выдачей книг.
    Пользователь может взять книгу (POST) и посмотреть свои книги (GET).
    """

    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Обработка для генерации Swagger-документации
        if getattr(self, "swagger_fake_view", False):
            return Loan.objects.none()
        # Обычный юзер видит только свои книги, админ — все
        user = self.request.user
        if user.is_staff:
            return Loan.objects.all()
        return Loan.objects.filter(user=user)

    def perform_create(self, serializer):
        # Автоматически привязываем текущего юзера к выдаче
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["post"])
    def return_book(self, request, pk=None):
        """Эндпоинт для возврата книги: /api/loans/{id}/return_book/"""
        loan = self.get_object()

        # Проверяем, что возвращает тот, кто взял (или админ)
        if loan.user != request.user and not request.user.is_staff:
            return Response(
                {"error": "Нельзя вернуть чужую книгу"},
                status=status.HTTP_403_FORBIDDEN,
            )

        if not loan.is_active:
            return Response(
                {"message": "Книга уже возвращена"}, status=status.HTTP_400_BAD_REQUEST
            )

        loan.return_book()
        return Response({"status": "Книга возвращена"}, status=status.HTTP_200_OK)
