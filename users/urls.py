from rest_framework.routers import DefaultRouter
from .views import UserRegistrationViewSet

router = DefaultRouter()
router.register(r'register', UserRegistrationViewSet, basename='register')

urlpatterns = router.urls