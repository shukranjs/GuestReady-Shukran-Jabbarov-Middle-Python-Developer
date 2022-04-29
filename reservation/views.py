from rest_framework import generics
from reservation.models import Rental, Reservation
from reservation.serializers import RentalSerializer, ReservationListSerializer, ReservationCreateSerializer
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import status


class ReservationListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = Reservation.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ReservationListSerializer
        else:
            return ReservationCreateSerializer


class RentalListAPIView(generics.ListAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
