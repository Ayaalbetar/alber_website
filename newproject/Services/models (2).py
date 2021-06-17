from django.core.files.storage import  *
from django.db import models

# Create your models here.
class Services (models.Model):
    name=models.CharField(max_length=40)
    def __str__(self):
        return  self.name
    class Meta:
        verbose_name ="الخدمات"



class Service_details (models.Model):
    name= models.CharField(max_length=40)
    status=models.BooleanField()
    types=models.CharField(max_length=1)
    idservice=models.ForeignKey(Services,related_name='contain',on_delete=models.CASCADE)

    def __str__(self):
        return self.name


from datetime import date
class Person(models.Model):
      isseen=models.BooleanField(default=False)
      fname =models.CharField(max_length=40)
      pname =models.CharField(max_length=30)
      mname =models.CharField(max_length=40)
      motherln=models.CharField(max_length=40)
      lname =models.CharField(max_length= 40)
      phone =models.IntegerField()
      id_namber=models.PositiveIntegerField()
      address =models.CharField(max_length=100,null=True)
      place_birth=models.CharField(max_length=30,null=True,default=None)
      gender =models.CharField(max_length=20,null=True ,default='')
      hasbend =models.CharField(max_length=30,null=True,default='')
      fhasbend = models.CharField(max_length=30,null=True ,default=None)
      card_number = models.PositiveIntegerField(null=True,default=0)
      percentage_health=models.PositiveIntegerField(null=True, default=0)
      count_child =models.PositiveIntegerField(null=True, default=0)
      amount_money=models.DecimalField(max_digits=6, decimal_places=2,default=0)
      assistance =models.ManyToManyField(Service_details, through='Request')
      birthday=models.DateField(default=date.today, null=True)
      nationality=models.CharField( max_length=30, default='سورية')
      father_die =models.BooleanField( default='False')
      # assistance = models.CharField(max_length=40, null='True')
      def user_directory_path(instance, filename):
          # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
          return 'user_{0}/{1}'.format(instance.id_namber, filename)
      photo =models.FileField(upload_to=user_directory_path, null='True')
      #fs = FileSystemStorage(location='/media/photos')
      #photo2=models.ImageField(storage=fs,upload_to=fs)


      def __str__(self):
        return  self.fname

      class Meta:
          verbose_name="المستفيد"
          verbose_name_plural ="المستفيدين"

# def user_directory_path(instance, filename):
#      # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
 #         return 'user_{0}/{1}'.format(instance.id_namber, filename)
#   photo =models.ImageField(upload_to=user_directory_path, null='True')


     # def full_name(self):
          #"Returns the person's full name."
      #    return '%s %s' % (self.first_name, self.last_name)

 # photo =models.ImageField(upload_to=' photos/%s/' % str(id_namber)  ,null='True')





class Request(models.Model):
    idperson =models.ForeignKey(Person,related_name='order',on_delete=models.CASCADE)
    idd =models.ForeignKey(Service_details,related_name='order',on_delete=models.CASCADE)
    request_date =models.DateTimeField(auto_now_add=True)
    request_place = models.CharField(max_length=40 ,null=True)
    status =models.SmallIntegerField(null=True)
    class Meta:
        verbose_name="الطلبات"


class Advertising(models.Model):
    title=models.CharField(max_length=500)
    details=models.TextField(max_length=3000)
    date=models.DateField(auto_now_add=True)
    photo=models.ImageField(upload_to="photo/%Y/%m/%d/",null=True)


class test (models.Model):
    name=models.CharField(max_length=30)
    file= models.FileField(upload_to="",null=True)