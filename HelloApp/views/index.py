__author__ = 'aleksandr.lavrik'

from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    context = RequestContext(request)
    return render_to_response(
        'index.html',
        {'param1': 'param1', 'param2': 'param2'},
        context)


