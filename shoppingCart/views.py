from django.http import HttpResponse


def home_page(views):
    return HttpResponse("Response is Ok")