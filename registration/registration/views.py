from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello, World!',im at Nairobi")
def register(request):
    return HttpResponse("This is the about page")
    