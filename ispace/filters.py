import django_filters
from .models import DepenseAvicole, Bande, CategorieDepense

class DepenseAvicoleFilter(django_filters.FilterSet):
    date_range = django_filters.DateFromToRangeFilter(
        field_name='date',
        label='Période (du - au)',
        widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'})
    )
    
    bande = django_filters.ModelChoiceFilter(
        queryset=Bande.objects.all(),
        label='Bande',
        field_name='bande'
    )
    
    categorie = django_filters.ModelChoiceFilter(
        queryset=CategorieDepense.objects.all(),
        label='Catégorie'
    )
    
    class Meta:
        model = DepenseAvicole
        fields = ['bande', 'categorie']