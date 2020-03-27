import json

import requests

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.defaultfilters import upper
from django.template.loader import render_to_string


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
        context['deaths'] = historic['timeline']['deaths'].values()
        context['historic'] = historic

        # print("Par: ", selected_country_info[0])

        html = render_to_string(
            template_name="countries-historical-partial.html", context=context
        )
        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)


    return render(request, 'historic.html', {'countries': countries})