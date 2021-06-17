from django.contrib import admin
from .models import  Services ,Service_details,Person,Request,Advertising
# Register your models here.
admin.site.register(Services)
admin.site.register(Service_details)

class AdminRrquest(admin.ModelAdmin):
    fields = []
    f=['request_date','status','idd',]
    list_display = f
    list_filter = f

   # def show(self):
    #    d=Request.Objects.filter(idd=1).count()
admin.site.register(Request,AdminRrquest)



class AdminPerson(admin.ModelAdmin):
    fields = []
    ff=['fname','id_namber','amount_money','isseen']
    f=['amount_money']
    f1 = ['fname',  ]
    list_display = ff
    list_display_links =f1
    f3=['isseen','amount_money']
    list_editable = f3
    list_filter = f3
    search_fields = ff



admin.site.register(Person,AdminPerson)
admin.site.register(Advertising)