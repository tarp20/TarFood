from rest_framework import serializers

from TarFoodApp.models import Restaurant

class RestaurantSerializers(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
