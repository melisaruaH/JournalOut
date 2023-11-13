from django.shortcuts import HttpResponse


def index(request):

    return HttpResponse("<h1>JournalOUT</h1>")