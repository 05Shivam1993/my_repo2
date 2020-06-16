from django.shortcuts import render
import datetime
from django.contrib import messages
from django.http import FileResponse
# Create your views here.

def index(request):
    date = datetime.datetime.now()
    return render(request,'portfolio.html',{'year':date.year})

def ViewFullCV(request):
    try:
        return FileResponse(open('media/Shivam_CV.pdf', 'rb'), content_type='application/pdf')
    except Exception as e:
        messages.warning(request,e)
    return redirect('/')
