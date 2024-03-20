from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line

def home(request):
    return HttpResponse("<h1>Welcome to the Home Page</h1><p>This is the home page.</p><p><a href='/about'>About</a></p>")

def about(request):
    return HttpResponse("<h1>About Us</h1><p>This is the about page.</p><p><a href='/'>Home</a></p>")

urlpatterns = [
    path('', home),
    path('about/', about),
]

if __name__ == "__main__":
    execute_from_command_line(["manage.py", "runserver", "localhost:1235"])
