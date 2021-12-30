from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Pizza

# Create your views here.


def index(request, pid):
    try:
        pizza = Pizza.objects.get(id=pid)
        return HttpResponse(
            content={
                'id': pizza.id,
                'title': pizza.title,
                'description': pizza.description,
            }
        )
    except Pizza.DoesNotExist:
        return HttpResponse(
            status_code=404,
            content={
                'status': 'error',
                'message': 'pizza not found',
            }
        )


def random(request):
    pizza = Pizza.objects.order_by('?')[0]
    return HttpResponse(
        content={
            'id': pizza.id,
            'title': pizza.title,
            'description': pizza.description,
        }
    )


class GetTenPizzasView(View):
    template_name = 'ten_pizzas.html'

    def get(self, request):
        pizzas = Pizza.objects.order_by('?')[:10]
        return render(request, self.template_name, {'pizzas': pizzas})
