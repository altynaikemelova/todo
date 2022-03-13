from django.shortcuts import render,HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("Добро пожаловать в приложение ToDo Admin! ")


def test(request):
    return render(request, "test.html")