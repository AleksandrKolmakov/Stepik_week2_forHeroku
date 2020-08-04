import random

from django.shortcuts import render
from django.http import Http404
from django.views import View

from data import tours, departures, description, subtitle, title


# Create your views here.


class MainView(View):
    def get(self, request):
        TOURS_RANDOM_COUNT = 6
        tour_id_list = []
        for key in tours.keys():
            tour_id_list.append(key)  # получили список id туров, теперь из этого списка получаем шесть случайных чисел
        if len(tour_id_list) > TOURS_RANDOM_COUNT:
            tour_id_list = random.sample(tour_id_list, TOURS_RANDOM_COUNT)

        # словарь, в котором случайные туры, если их более 6
        random_dict = {}
        for id in tour_id_list:
            random_dict[id] = tours[id]

        context = {
            'title': title,
            'subtitle': subtitle,
            'description': description,
            'random_dict': random_dict
        }
        return render(request, 'tours/index.html', context=context)


class DepartureView(View):
    def get(self, request, departure):
        if departure not in departures.keys():
            raise Http404
        # в контекст нужно передать также список туров для данного направления, можно сразу посчитать статистику
        # Туры по направлению и статистика по ним
        dep_tours = {}
        prices = set()
        nights = set()
        for id, tour in tours.items():
            if tour['departure'] == departure:
                dep_tours[id] = tours[id]
                prices.add(tour['price'])
                nights.add(tour['nights'])

        # подсчет статистики
        stats = {}
        # всего туров, цена мин, цена макс, ночей мин и ночей макс
        stats['tour_count'] = len(dep_tours)
        stats['min_price'] = min(prices)
        stats['max_price'] = max(prices)
        stats['min_nights'] = min(nights)
        stats['max_nights'] = max(nights)

        context = {
            'departure': departures[departure],
            'dep_tours': dep_tours,
            'stats': stats
        }
        return render(request, 'tours/departure.html', context=context)


class TourView(View):
    def get(self, request, id):
        if id not in tours.keys():
            raise Http404
        departure = departures[tours[id]["departure"]]
        context = {
            'tour': tours[id],
            'departure': departure
        }
        return render(request, 'tours/tour.html', context=context)


def my_custom_page_404(request, exception=None):
    return render(request, 'tours/404.html')


def my_custom_page_500(request, exception=None):
    return render(request, 'tours/500.html')
