from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import GlobalSearchView, BookViewSet, LoanViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r"books", BookViewSet, basename="book")
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r"loans", LoanViewSet, basename="loan")

urlpatterns = [
    path('search/', GlobalSearchView.as_view(), name='global-search'),
] + router.urls
