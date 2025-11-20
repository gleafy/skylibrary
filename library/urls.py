from rest_framework.routers import DefaultRouter
from .views import BookViewSet, LoanViewSet, UserRegistrationViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'loans', LoanViewSet, basename='loan')
router.register(r'register', UserRegistrationViewSet, basename='register')

urlpatterns = router.urls
