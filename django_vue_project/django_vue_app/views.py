from django.http import HttpResponse
from django.views import View

class HomeView(View):
    def get(self, request):
        # Implement the API endpoint for product management here
        return HttpResponse('Hello, this is the home page of django_vue_app.')