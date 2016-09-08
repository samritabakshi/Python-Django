from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.exceptions import *


# Create your views here.
from django.views.generic import TemplateView

from .forms import myForm
import time

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
       return render(request, 'index.html', context=None)
#class AboutPageView(TemplateView):
 #   template_name = "about.html"
#template_name = "about.html"

class takeInput(TemplateView):
	form_class = myForm
    	initial = {'key': 'value'}
    	template_name = 'form_template.html'
	def post(self, request, *args, **kwargs):
	    form = self.form_class(request.POST)
	    print "******" 
	    print request
	    if request.method == 'POST':
		n = request.POST['text']

		startTime = time.clock()
		if n < 0:
		    print 'Enter a positive number'
		else:
		    if n == 1:
		        print n
		    else:
		        a = 0
		        b = 1
		        c = a + b
		        count = 0
		        print 'Fibonacci sequence:'
		        print a
		        print b
		        while count <= n:
		            c = a + b
		            print c
		            a = b
		            b = c
		            count += 1

		print time.clock() - startTime, 'seconds'
		


			
