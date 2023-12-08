from django.shortcuts import render

# Create your views here.
def lovely(request):
    return render(request,'lovely.html')
