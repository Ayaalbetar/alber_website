from django.urls import path
from . import views
urlpatterns=[
    path('services',views.services,name='services'),
    path('',views.index,name='index'),
    path('services/<int:services_id>/',views.services_details,name='services_details'),
    path('services/<int:services_id>/new',views.newperson,name='newperson'),
   # path('services/1/1', views.newstudent, name='newstudent'),
   # path('services/1/2', views.neworphan,name='neworphan'),
   # path('services/1/3', views.newfamily, name='newfamily'),
    #path('services/2/1', views.newmedicine, name='newmwdicine'),
#  path('services/<int:s_id>/1',views)
    path('i',views.testt,name='test')
  ]