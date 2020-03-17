import django_filters

from lesson_nine import models


class ProductFilter(django_filters.FilterSet):

    ORDER_CHOICE = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )

    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    search = django_filters.CharFilter(field_name='name', lookup_expr='contains')

    ordering = django_filters.ChoiceFilter(label='ordering',
                                           choices=ORDER_CHOICE,
                                           method='filter_by_order')

    category = django_filters.ModelMultipleChoiceFilter(queryset=models.Categories.objects.all())

    class Meta:
        model = models.Product
        fields = ['ordering', 'price__gt', 'price__lt', 'category', 'search']

    def filter_by_order(self, queryset, name, value):
        expression = 'price' if value == 'descending' else '-price'
        return queryset.order_by(expression)
    #
    # class Meta:
    #     model = models.Product
    #     fields = {
    #         'price': ['lt', 'gt'],
    #     }
