from django.shortcuts import render,redirect
from  django.contrib import messages
from Services.models import Person,Request,Service_details
import  re


########################################################

import  os
from django.http import HttpResponse
import mimetypes

def download_image(request, image_id):
    img = Person.objects.get(id=image_id)
    wrapper      = open(img.file)  # img.file returns full path to the image
    content_type = mimetypes.guess_type("photo")[0]  # Use mimetypes to get file type
    response     = HttpResponse(wrapper,content_type=content_type)
    response['Content-Length']      = os.path.getsize(img.file)
    response['Content-Disposition'] = "attachment; filename=%s" %  img.name
    return response
#########################################################















# Create your views here.
def newstudent(request,):
   if request.method =='POST' and 'btnsign' in  request.POST:

       # variabls for  fields
       fname=None
       lname =None
       place_birth=None
       birthday = None
       gender=None
       pname=None
       mname=None
       motherln=  None
       nationality=None
       id_namber=None
       phone =None
       address=None
       fatherdie =None
       photo1=None
       is_added=None # من اجل ان نختر هل تم الاضافة



       # Get  values from the form
       if 'fname' in request.POST:
           fname = request.POST['fname']
       else:
           messages.error(request, 'error in fname')


       if 'bornplace' in request.POST:
           place_birth = request.POST['bornplace']
       else:
           messages.error(request, 'error in bornplace')

       if 'lname' in request.POST:
           lname = request.POST['lname']
       else:
           messages.error(request, 'error in lname')


       #if 'birthday' in request.POST:
        #    birthday = request.POST['birthday']
       #else:
        #   messages.error(request, 'خطأ في المواليد')


       if 'pname' in request.POST:
           pname = request.POST['pname']
       else:
           messages.error(request, 'هخطأ فياسم الاب')


       if 'motherln' in request.POST:
           motherln = request.POST['motherln']
       else:
           messages.error(request, 'خطأ في عدم ادخال نسبة الأم')

       if 'id_namber' in request.POST:
           id_namber = request.POST['id_namber']
       else:
           messages.error(request, 'خطأ في عدم ادخال الرقم الوطني')

       if 'nationality' in request.POST:
           nationality = request.POST['nationality']
       else:
           messages.error(request, 'خطأ في عدم ادخال الجنسية ')

       if 'phone' in request.POST:
           phone = request.POST['phone']
       else:
           messages.error(request, 'error in phone')

       if 'address' in request.POST:
           address = request.POST['address']
       else:
           messages.error(request, 'error in address')

       if 'mname' in request.POST: mname = request.POST['mname']
       else: messages.error(request, 'اسم الام')

       if  'f1' in request.POST and 'f2' in request.POST :photo1=[request.POST['f1'],request.POST['f2']]
       else:messages.error(request,'phooooooootos')

       if 'father_die'in request.POST:fatherdie=request.POST['father_die']
       #gender=request.POST['Radios1']

       if 'Radios1' in request.POST:gender=request.POST['Radios1']
       #elif 'Radios2' in request.POST: gender=request.POST['Radios2']

# check the value:
       if  fname and lname and mname and pname and place_birth and gender and phone and address and nationality and id_namber and motherln :
           if fatherdie ==True:
              pass
# chek if id_naber is uniqc and user is token
           if Person.objects.filter(id_namber=id_namber).exists():
               messages.error(request,'لقد سجلت مسبقا!!! ')
           else:
               #add student profile
               def user_directory_path(instance, filename):
                   # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
                   return 'user_{0}/{1}'.format(instance.id_namber, filename)


               student=Person(fname=fname,lname=lname,pname=pname,mname=mname,address=address,motherln=motherln,phone=phone,nationality=nationality,
                          id_namber=id_namber,place_birth=place_birth,gender=gender,birthday=birthday,)
                               #photo=user_directory_path(Person.objects.set(id_namber=id_namber),"user")
                            #father_die=fatherdie
                         #)
               student.save()
               is_added=True

               id1=Person.objects.get(fname=fname,lname=lname,pname=pname,mname=mname,address=address,motherln=motherln,phone=phone,nationality=nationality,
                          id_namber=id_namber,place_birth=place_birth,gender=gender,birthday=birthday)
               fname = '',
               lname = '' ,
               pname = ' ',
               mname =  ' ',
               address = ' ',
               motherln = ' ',
               phone = ' ',
               nationality = ' ',
               id_namber = ' ',
               place_birth = ' ',
               gender = ' ',
               birthday = ' ',
               fatherdie = ' '
               id2=Service_details.objects.get( name='كفالة طالب علم',status=True)
               req=Request( idperson=id1,idd=id2,request_place=None ,status=1)
               req.save()

               # sucsses messages
               messages.success(request,'تم تسجيل طلبك ستصلك رسالة ')

       else: messages.error(request,'هناك حقول فارغة ')
       context ={
              'fname':fname,
             'lname':lname,
             'pname':pname,
             'mname':mname,
             'address':address,
             'motherln':motherln,
             'phone':phone,
             'nationality':nationality,
             'id_namber':id_namber,
             'place_pirth':place_birth,
             'gender':gender,
             'birthday':birthday,
             'father_die':fatherdie,
              'is_added':is_added
       }
       return render(request, 'pages/newstudent.html', context)
   else:
   # messages.info(request, 'لقد تم تسجيل طلبك ')
    context={ }
   return render(request,'pages/newstudent.html',context)
# -------------------------
def neworphan(request):
    context ={}

    return render(request,'pages/neworphan.html',context)
#-------------------------
def newfamily(request):
    context={}
    return render(request,'pages/newfamily.html',context)

#-------------------------
def newmedicine(request):
    context={}
    return render(request,'pages/newmedicine.html',context)
