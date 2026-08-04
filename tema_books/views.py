from django.http import HttpResponse, HttpRequest
import random

# Create your views here.

names = [
    "Andrei", "Maria", "Ion", "Elena", "Alexandru", "Ana",
    "Vasile", "Ioana", "George", "Gabriela", "Florin", "Mihai",
    "Diana", "Radu", "Laura", "Cristian", "Raluca",
    "Bianca",
]

numbers = [73, 28, 95, 14, 61, 39, 87, 5, 46, 32, 345, 232, 12, 33, 99, 96, 35, 1, 9, 10]


def list_names(request: HttpRequest):
    sorted_names = sorted(names)
    result = ", ".join(sorted_names)
    return HttpResponse(result)

def list_numbers(request: HttpRequest):
    sorted_numbers = sorted(numbers, reverse=True)
    str_numbers = [str(n) for n in sorted_numbers]
    result = ", ".join(str_numbers)
    return HttpResponse(result)

def list_paired_names(request: HttpRequest):
    data = [{"name": name, "count": random.choice(numbers)} for name in names]
    result = str(data)
    return HttpResponse(result)