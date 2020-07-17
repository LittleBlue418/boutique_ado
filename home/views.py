from django.shortcuts import render


# View to return the index page
def index(request):
    return render(request, 'home/index.html')
