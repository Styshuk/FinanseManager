from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from apps.manager.models import Operation


def get_all_operation(request):
    if request.method == "GET":
        operations = Operation.objects.all()
        return render(request, "all_operations.html",
                      context={"title": "All Operation",
                               "operations": operations})


def get_all_incomes(request):
    if request.method == "GET":
        operations = Operation.objects.filter(type_id=1)
        return render(request, "all_operations.html",
                      context={"title": "All Incomes",
                               "operations": operations})


def get_all_consumptions(request):
    if request.method == "GET":
        operations = Operation.objects.filter(type_id=2)
        return render(request, "all_operations.html",
                      context={"title": "All Consumptions",
                               "operations": operations})
