from django.http import HttpResponse

def handler404(request, exception):
    return HttpResponse("Route Not Found!")

def handler403(request, *args, **argv):
    return HttpResponse("Method Not Available!")