from django.shortcuts import render, redirect
#For importing datetime
import datetime
# Create your views here.
from django.http import HttpResponse
#For CURD in curdops
from myapp.models import Dreamreal
#For sending email
from django.core.mail import send_mail
#For generic views
from django.views.generic import TemplateView
#For forms
from myapp.forms import LoginForm

class Staticview(TemplateView):
	template_name = "static.html"

def hello(request):
	#text = """<h1>welcome to my app !</h1>"""
	today = datetime.datetime.now().date()
	time = datetime.datetime.now().time()
	daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
	# return render(request, 'hello.html', {"today":today, "time":time, "daysOfWeek": daysOfWeek})
	return redirect("https://www.djangoproject.com")

def viewArticle(request, articleID):
	text = "Displaying article Number : %s"%articleID
	# return HttpResponse(text)
	return redirect(viewArticles, year = "2045", month = "02")

def viewArticles(request, month, year):
	text = "Displaying articles of :" + str(month) + '/' + str(year)
	return HttpResponse(text)

def crudops(request):
   #Creating an entry
   
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   
   #Read ALL entries
   objects = Dreamreal.objects.all()
   res ='Printing all Dreamreal entries in the DB : <br>'
   
   for elt in objects:
      res += elt.name+"<br>"
   
   #Read a specific entry:
   sorex = Dreamreal.objects.get(name = "sorex")
   res += 'Printing One entry <br>'
   res += sorex.name
   
   #Delete an entry
   res += '<br> Deleting an entry <br>'
   sorex.delete()
   
   #Update
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   res += 'Updating entry<br>'
   
   dreamreal = Dreamreal.objects.get(name = 'sorex')
   dreamreal.name = 'thierry'
   dreamreal.save()

   return HttpResponse(res)

def datamanipulation(request):
   res = ''
   
   #Filtering data:
   qs = Dreamreal.objects.filter(name = "paul")
   res += "Found : %s results<br>"%len(qs)
   
   #Ordering results
   qs = Dreamreal.objects.order_by("name")
   
   for elt in qs:
      res += elt.name + '<br>'
   
   return HttpResponse(res)

def sendSimpleEmail(request,emailto):
   res = send_mail("hello paul", "how are you?", "paul@polo.com", [emailto])
   return HttpResponse('%s'%res)

def login(request):
   username = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
   else:
      MyLoginForm = Loginform()
		
   return render(request, 'loggedin.html', {"username" : username})