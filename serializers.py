from rest_framework import serializers
from .models import MenuItem, Customer, Reservation
import datetime
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
class ReservationSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = Reservation
        fields = '__all__'
    def validate(self, data):
        # basic field validation
        if data['date'] < datetime.date.today():
            raise serializers.ValidationError({'date':'Reservation date must be today or in the future.'})
        if data['party_size'] < 1:
            raise serializers.ValidationError({'party_size':'Party size must be at least 1.'})
        # check for exact datetime collision (same date and time)
        date = data.get('date')
        time = data.get('time')
        qs = Reservation.objects.filter(date=date, time=time)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError({'non_field_errors':'A reservation already exists at this date and time. Please choose another slot.'})
        return data
    def create(self, validated_data):
        cust_data = validated_data.pop('customer')
        customer, _ = Customer.objects.get_or_create(email=cust_data.get('email'), defaults=cust_data)
        reservation = Reservation.objects.create(customer=customer, **validated_data)
        return reservation
