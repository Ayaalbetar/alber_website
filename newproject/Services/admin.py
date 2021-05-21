from django.contrib import admin
from .models import  Services ,Service_details,Person,Request
# Register your models here.
admin.site.register(Services)
admin.site.register(Service_details)
admin.site.register(Person)
admin.site.register(Request)