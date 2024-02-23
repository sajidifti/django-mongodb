from .models import person_collection
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<h1>App is running</h1>")


def add_person(request):
    records = {"name": "Sajid Anam Ifti", "age": 24}
    person_collection.insert_one(records)

    return HttpResponse("<h1>Person added successfully</h1>")


def get_all_persons(request):
    persons = person_collection.find()
    return HttpResponse(persons)
