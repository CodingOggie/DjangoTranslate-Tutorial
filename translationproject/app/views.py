from django.shortcuts import render
from django.utils.translation import gettext as _


def index(request):
    example_sentence = 'Welcome to my site.'

    # example_variable = _(example_sentence)

    context = {
        'sentence': example_sentence
    }
    return render(request, 'index.html', context=context)
