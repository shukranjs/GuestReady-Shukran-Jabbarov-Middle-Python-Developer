from django.contrib import admin
from . models import Reservation, Rental


admin.site.register(Reservation)
admin.site.register(Rental)
