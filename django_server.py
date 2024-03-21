from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line
from django.conf import settings

# Django views
def home(request):
    return HttpResponse(
        "<html><body>"
        "<h1>Welcome to the Home Page</h1>"
        "<p>This is the home page.</p>"
        "<p><a href='/about'>About</a></p>"
        "</body></html>"
    )

def about(request):
    return HttpResponse(
        "<html><body>"
        "<h1>About Us</h1>"
        "<p>This is the about page.</p>"
        "<p><a href='/'>Home</a></p>"
        "</body></html>"
    )

# Django URL patterns
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
]

# Django settings
settings.configure(
    DEBUG=True,
    SECRET_KEY='your_secret_key',
    ROOT_URLCONF=__name__,
)

if __name__ == "__main__":
    # Run Django development server
    execute_from_command_line(["web_server.py", "runserver"])
