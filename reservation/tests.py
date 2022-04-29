from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from .factories import ReservationFactory, RentalFactory



class TestReservation(TestCase):

    def test_reservation_create(self):
        rental = RentalFactory()

        data = {
            "rental_id": rental.id,
            "checkin": "2019-01-01",
            "checkout": "2019-01-02"
        }

        response = self.client.post(reverse('reservation-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['rental_id'] == rental.id
        assert response.data['checkin'] == data["checkin"]
        assert response.data['checkout'] == data["checkout"]

    def test_reservation_create_checkin_date_must_be_unique(self):

        rental = RentalFactory()

        data = {
            "rental_id": rental.id,
            "checkin": "2019-01-01",
            "checkout": "2019-01-02"
        }

        response = self.client.post(reverse('reservation-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['rental_id'] == rental.id
        assert response.data['checkin'] == data["checkin"]
        assert response.data['checkout'] == data["checkout"]

        response = self.client.post(reverse('reservation-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {'non_field_errors': ['Reservation already exists']})

    def test_reservation_create_checkout_date_must_be_greater_than_checkin_date(self):
        rental = RentalFactory()
        data = {
            "rental_id": rental.id,
            "checkin": "2019-01-01",
            "checkout": "2019-01-01"
        }

        response = self.client.post(reverse('reservation-list'), data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {'non_field_errors': ['Checkin date must be before checkout date']}

    def test_reservation_list_previous_reservation_id(self):
        reservation_1 = ReservationFactory(checkin="2020-01-01", checkout="2020-01-02")
        response = self.client.get(reverse('reservation-list'))
        assert response.status_code == status.HTTP_200_OK
        assert response.json()[0]['previous_reservation_id'] == '-'
        ReservationFactory(checkin="2020-01-03", checkout="2020-01-04", rental_id=reservation_1.rental_id)
        response = self.client.get(reverse('reservation-list'))
        assert response.status_code == status.HTTP_200_OK
        assert response.json()[0]['previous_reservation_id'] == reservation_1.id

    def test_reservation_list_empty(self):
        response = self.client.get(reverse('reservation-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 0

    def test_reservation_list_success(self):
        ReservationFactory()
        response = self.client.get(reverse('reservation-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
