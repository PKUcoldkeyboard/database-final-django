from django_filters import rest_framework as filters
import bookstore.models as models

class BmsBookFilter(filters.FilterSet):

    class Meta:
        model = models.BmsBook
        fields = {
            'name':['icontains'],
            'price':['gte','lte'],
        }