from django.urls import path, include
from .views import BookViewSet, CustomAuthToken
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Book', BookViewSet)
urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('api/', include(router.urls))

]