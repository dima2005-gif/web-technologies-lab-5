from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Це головна сторінка магазину.")
