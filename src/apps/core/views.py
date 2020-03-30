import json

import requests

from django.http import JsonResponse
from django.shortcuts import render

import numpy as np

# Create your views here.
from django.template.defaultfilters import upper
from django.template.loader import render_to_string

from apps.utils.cases import get_scenario_on_day


def home(request):

    countries = requests.get('https://corona.lmao.ninja/countries').json()

    url_parameter = request.GET.get("q")

    if url_parameter != None:
        countries = [ct for ct in countries if upper(url_parameter) in upper(ct['country'])]

    if request.is_ajax():
        html = render_to_string(
            template_name="countries-results-partial.html",
            context={"dados": countries}
        )
        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'home.html', {'dados': countries})


def historico(request):
    historics = requests.get('https://corona.lmao.ninja/historical').json()
    countries = requests.get('https://corona.lmao.ninja/countries').json()

    if request.is_ajax():

        context = {}

        selected_country = request.GET.get('sortBy')

        historic = requests.get(f'https://corona.lmao.ninja/v2/historical/{selected_country}').json()

        context['dates'] = historic['timeline']['cases']
        context['cases'] = list(context['dates'].values())
        context['casesOnDay'] = get_scenario_on_day(context['cases'])
        context['deaths'] = list(historic['timeline']['deaths'].values())
        context['deathsOnDay'] = get_scenario_on_day(context['deaths'])
        context['historic'] = historic

        html = render_to_string(
            template_name="countries-historical-partial.html", context=context
        )
        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)


    return render(request, 'historic.html', {'countries': countries})