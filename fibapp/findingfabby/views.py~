from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.exceptions import *
from django.template import Context
from django.http import HttpResponse


# Create your views here.
from django.views.generic import TemplateView

#from .forms import myForm
import time

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
       return render(request, 'index.html')
class AboutPageView(TemplateView):
   template_name = "about.html"
#template_name = "about.html"

class takeInput(TemplateView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
		n = request.POST['no']
		timeTaken = 0 
		print 'Number Sent in Request1->'
		print  n
		nu = int(n)
		startTime = time.clock()
		res='0,1'
		if nu < 0:
		    print 'Enter a positive number'
		elif nu == 1:
		    print nu
		else:
		    a = 0
		    b = 1
		    c = a + b
		    count = 0
		    print 'Fibonacci sequence:'
		    print a
		    print b
		    while count < nu-2:
		        c = a + b
		        res= res + ',' + str(c)
		        a = b
		        b = c
		        count += 1
		print 'Fibonacci Series is->'
		print res
		timeTaken+= time.clock()-startTime  
	
	res=res + " Time Taken -->" + str(timeTaken) + "seconds"	
	return HttpResponse(res)
			
			
