from django.shortcuts import render
from django.utils.translation import gettext as _
import random


def index(request):
    # 1. show simple translation
    # 2. show manage.py (and install gettext)
    # 3. show compile.py
    example_sentence = _('Welcome to my site.')

    m = 2
    d = 13

    example_variable_sentence = _('Today is %(month)s %(day)s.') % {
        'month': m, 'day': d}

    # example_variable = _(example_sentence)

    context = {
        'sentence': example_sentence,
        'random_int': random.random(),
        'example_variable_sentence': example_variable_sentence
    }
    return render(request, 'index.html', context=context)
