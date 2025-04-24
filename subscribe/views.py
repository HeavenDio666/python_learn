from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world ! ")

# http://localhost:5173/#/login