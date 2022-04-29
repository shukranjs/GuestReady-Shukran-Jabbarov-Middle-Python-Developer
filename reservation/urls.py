from django.urls import path, include
from rest_framework import routers
from.views import ReservationListCreateAPIView, RentalListAPIView
router = routers.DefaultRouter()

router.register('reservations', ReservationListCreateAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('rentals/', RentalListAPIView.as_view()),
]