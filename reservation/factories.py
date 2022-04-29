import factory
from factory.django import DjangoModelFactory


class RentalFactory(DjangoModelFactory):
    class Meta:
        model = 'reservation.Rental'

    name = 'Test Rental'


class ReservationFactory(DjangoModelFactory):
    class Meta:
        model = 'reservation.Reservation'

    rental_id = factory.SubFactory(RentalFactory)
    checkin = '2020-01-01'
    checkout = '2020-01-02'
