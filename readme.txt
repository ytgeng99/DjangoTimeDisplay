Assignment: Time Display
Create a Django app called time_display according to the below wireframe.

alt text

In timedisplay's controller (apps/time_display/views.py), create a method named index.

When you go to the URL localhost:8000 or localhost:8000/time_display/ this should run the index method in your controller file, (views.py). Have that method render a template that displays the current date and time.

from django.shortcuts import render, HttpResponse, redirect
def yourMethodFromUrls(request):
  context = {
  "somekey":"somevalue"
  }
  return render(request,'appname/page.html', context)
The keys of your context dictionary are available to be accessed on your page.html.

<div class="line">{{somekey}}</div>
The above line will print out “somevalue” on your HTML!

To see how you can get the current time in Python, you could for example make sure views.py import gmtime, strftime from 'time' and pass the appropriate string to the render method.  For example, your views.py could look like:

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
  context = {
  "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
  }
  return render(request,'appname/index.html', context)
To learn more about strftime, see https://docs.python.org/3.3/library/time.html?highlight=time.strftime#time.strftime

Please also see https://stackoverflow.com/questions/466345/converting-string-into-datetime