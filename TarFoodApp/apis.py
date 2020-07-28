from django.http import JsonResponse

from TarFoodApp.models import Restaurant
from TarFoodApp.serializers import RestaurantSerializers

def customer_get_restaurants(request):
    restaurant = RestaurantSerializers(
        Restaurant.objects.all().order_by("-id"),
        many=True,
    ).data

    return JsonResponse({"restaurant": restaurant})

