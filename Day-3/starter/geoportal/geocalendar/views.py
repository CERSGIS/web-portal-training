from django.shortcuts import render

# Create your views here.
def calendar_view(request):
    return render(request, 'geocalendar/calendar.html')