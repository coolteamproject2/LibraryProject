from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

def home (request):
    return JsonResponse({'message': 'Welcome to the Book Library API'})

def health_check(request):
    return JsonResponse({'status': 'healthy'})

class BookListView(View):
    def get(self, request):
        # example data, just testing
        books = [
            {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
            {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
        ]
        return JsonResponse({'books': books})
    

