from django.db import models


class Rental(models.Model):

    name = models.CharField(max_length=127)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name


class Reservation(models.Model):

    rental_id = models.ForeignKey(Rental, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.rental_id.name
