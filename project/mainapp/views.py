from mainapp.models import Stuff
from django.shortcuts import render

from django.views.generic.list import ListView
from django_filters import FilterSet  #  не забываем добавить 'django_filters' в settings

# объявили фильтр через дженерик FilterSet
class StuffFilterSet(FilterSet):
    class Meta:
        model = Stuff
        fields = {
            'name': ['icontains']
        }


# объявляем основной view с переопределением queryset
class FilteredListView(ListView):
    model = Stuff
    template_name = 'mainapp/main.html'
    filterset_class = None  #  переменная в последующем будет включать в себя класс фильтра

    def get_queryset(self):
        #  Получаем queryset
        queryset = super().get_queryset()
        #  Переопределяем queryset через filterset, который пока None, но будет объявлен потом при наследовании
        self.filterset = self.filterset_class(
            self.request.GET, queryset=queryset)
        # Возвращаем отсортированный queryset
        return self.filterset.qs.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset  #  объявляем для шаблона способ обращения к отфильтрованному queryset
        context['all_stuff'] = Stuff.objects.all()  #  получаем количество всех наименований
        context['paginate'] = self.paginate_by  #  получаем количество всех наименований
        return context

#  наследуемся от FilteredListView и определяем FilterSet и пагинацию
class StuffView(FilteredListView):
    filterset_class = StuffFilterSet
    paginate_by = 2
