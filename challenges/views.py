from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


# def index(request):
#     return HttpResponse("Hello world")

def get_challenge_bynumber(request, month):
    data = "Nothing here"
    if month == 1:
        data = "in january"
    elif month == 2:
        data = "Testing in febuary"
    else:
        return HttpResponseNotFound("hey there an issue occured")
    return HttpResponse(data)


def get_Challenges(request, month):
    data = "Nothing here"
    if month == "january":
        data = "in january"
    elif month == "fabuary":
        data = "Testing in febuary"
    else:
        return HttpResponseNotFound("hey there an issue occured")
    return HttpResponse(data)
