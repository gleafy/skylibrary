from rest_framework import serializers
from .models import Book, Loan, Author, CustomUser


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author_info = AuthorSerializer(source='author', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_info', 'isbn', 'inventory_count']


class LoanSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    book_title = serializers.ReadOnlyField(source="book.title")

    class Meta:
        model = Loan
        fields = [
            "id",
            "user",
            "book",
            "book_title",
            "taken_at",
            "returned_at",
            "is_active",
        ]
        read_only_fields = ["returned_at", "is_active", "taken_at"]

    def validate_book(self, value):
        if value.inventory_count <= 0:
            raise serializers.ValidationError("Этой книги сейчас нет в наличии.")
        return value


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ("username", "password", "email")

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data.get("email", ""),
        )
        return user
