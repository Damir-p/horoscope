from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.

zodiac_dict = {

    'oven': '21 марта – 20 апреля',

    'telets': '21 апреля – 21 мая',

    'bliznetsy': '22 мая – 21 июня',

    'rak': '22 июня – 22 июля',

    'lev': '23 июля – 23 августа',

    'deva': '24 августа – 22 сентября',

    'vesy': '23 сентября – 23 октября',

    'scarpion': '24 октября – 22 ноября',

    'strelets': '23 ноября – 21 декабря',

    'kozerog': '22 декабря – 20 января',

    'vodoley': '21 января – 18 февраля',

    'ryby': '19 февраля = 20 марта',

}

def zodiac(request, sign_zodiac):

    discription = zodiac_dict.get(sign_zodiac, None)
    if discription:
        return HttpResponse(discription)
    else :
        HttpResponseNotFound(f'неизвестный знак зодиак!! - {sign_zodiac}')