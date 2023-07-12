import django_filters
from django_filters import *  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post


# создаём фильтр
class PostFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т.е. подбираться) информация о товарах
    # dateCreation = django_filters.CharFilter(label='Дата создания')
    class Meta:
        model = Post
        fields = {'dateCreation': ['gt'], 'title': ['icontains'], 'author': ['exact']}  # поля, которые мы будем фильтровать (т.е. отбирать по каким-то критериям, имена берутся из моделей)