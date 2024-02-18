# myapp/urls.py

from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, ShoppingHistoryViewSet

router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet, basename='userprofile')
router.register(r'shoppinghistory', ShoppingHistoryViewSet, basename='shoppinghistory')
urlpatterns = router.urls

# myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
]
