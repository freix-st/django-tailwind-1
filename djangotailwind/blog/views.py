from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inner_page(request):
    context = {
        'title': 'Inner Page',
        'content': 'This is the inner page',
    }
    return render(request, 'blog/inner-page.html', context)