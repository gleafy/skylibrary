from rest_framework import serializers
from .models import Book, Loan
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'inventory_count']


class LoanSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    book_title = serializers.ReadOnlyField(source='book.title')

    class Meta:
        model = Loan
        fields = ['id', 'user', 'book', 'book_title', 'taken_at', 'returned_at', 'is_active']
        read_only_fields = ['returned_at', 'is_active', 'taken_at']

    def validate_book(self, value):
        if value.inventory_count <= 0:
            raise serializers.ValidationError("Этой книги сейчас нет в наличии.")
        return value


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user
