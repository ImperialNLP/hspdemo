from django.shortcuts import render
from django.views import generic

import json

# Create your views here.


class Home(generic.TemplateView):
    template_name = 'todo/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


def demo(request):
    with open('example.json', 'r') as f:
        json_string = json.load(f)
    return render(request, 'todo/demo.html', {'json_string': json_string})

