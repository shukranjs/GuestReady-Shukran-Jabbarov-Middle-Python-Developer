from reservation.models import Rental, Reservation
from rest_framework import serializers


class RentalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rental
        fields = ('id', 'name',)


class ReservationListSerializer(serializers.ModelSerializer):

    rental_name = serializers.CharField(source='rental_id.name', read_only=True)
    previous_reservation_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Reservation
        fields = ('rental_name', 'id', 'checkin','checkout', 'previous_reservation_id')

    def get_previous_reservation_id(self, obj):
        last_reservation = obj.rental_id.reservation_set.order_by('id')
        if last_reservation.exclude(id=obj.id):
            position_of_obj = list(last_reservation.values_list('id', flat=True)).index(obj.id)
            if position_of_obj == 0:
                return '-'
            count_ = position_of_obj-1
            return last_reservation[(count_)].id

        return "-"


class ReservationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ('rental_id', 'checkin', 'checkout')

    def validate(self, data):
        rental_id = data.get('rental_id')
        checkin = data.get('checkin')
        checkout = data.get('checkout')
        if checkin < checkout:
            reservation = Reservation.objects.filter(
                rental_id=rental_id, checkin__lte=checkin, checkout__gte=checkout).first()
            if reservation:
                raise serializers.ValidationError("Reservation already exists")
            return data
        else:
            raise serializers.ValidationError("Checkin date must be before checkout date")
