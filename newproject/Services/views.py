from django.shortcuts import render,get_object_or_404
from .models import Services,Service_details,Person,Request
from django.http import HttpResponse

# Create your views here.
def index(request):
    #title= request.user
    title='جمعية البر والخدمات الاجتماعية '
    context={
        "template":title

    }
   # return HttpResponse('<H1 align="center">جمعية البر والخدمات الاجتماعية</h1>')
    return render(request,'index.html',context)

def i(request):
    return render(request,'test.html')


def services (request):


    services = Services.objects.all()
    s = Service_details.objects.all()
    context = {
        'services': services,
        's' : s,

      }

    return  render(request,'services.html', context)


def services_details(request,services_id):
   # services =Service_details.objects.get(pk=services_id)
   services=get_object_or_404(Services,pk=services_id)
   ss = Service_details.objects.all()
   context ={
      'services': services,
      'ss':  ss}
   return  render(request,'services_details.html', context)





#---------------------------------
def newstudent(request,):

    context={

    }
    return render(request,'pages/newstudent.html',context)
# -------------------------
def neworphan(request):
    context ={
    }

    return render(request,'pages/neworphan.html',context)
#-------------------------
def newfamily(request):
    context={}
    return render(request,'pages/newfamily.html',context)

#-------------------------
def newmedicine(request):
    context={}
    return render(request,'pages/newmedicine.html',context)


from .models import Person
from .forms import NewPersonForm
def newperson(request,services_id):
   # ser = get_object_or_404(Service_details, pk=services_id)
    form= NewPersonForm()

    return render(request,'newperson.html',{'form':form})

