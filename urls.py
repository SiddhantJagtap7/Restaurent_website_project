from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views  # Import views from the same app directory

# Create a router for our API ViewSets
router = DefaultRouter()
router.register(r'menu', views.MenuItemViewSet, basename='menu')
router.register(r'reservations', views.ReservationViewSet, basename='reservation')

# The API URLs are now determined automatically by the router.
# This will be included by the main urls.py under the 'api/' prefix.
urlpatterns = [
    path('', include(router.urls)),
]